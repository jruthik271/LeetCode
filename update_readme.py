import os
import re

def parse_existing_categories(readme_path):
    categories = {}
    if not os.path.exists(readme_path):
        return categories
        
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Find table between comment markers
    match = re.search(r"<!-- SOLUTIONS_START -->(.*?)<!-- SOLUTIONS_END -->", content, re.DOTALL)
    if not match:
        return categories
        
    table_content = match.group(1)
    for line in table_content.splitlines():
        # Table lines start with | and have columns separated by |
        if line.strip().startswith("|") and not "---" in line and not "#" in line:
            parts = [p.strip() for p in line.split("|")[1:-1]]
            if len(parts) >= 4:
                problem_id = parts[0]
                category = parts[3]
                categories[problem_id] = category
                
    return categories

def guess_category(py_file_path):
    if not os.path.exists(py_file_path):
        return "Unknown"
        
    with open(py_file_path, "r", encoding="utf-8") as f:
        code = f.read()
        
    # Simple heuristics based on common imports or keywords
    topics = []
    if "List[" in code or "List " in code or "List\n" in code:
        topics.append("Arrays")
    if "str" in code or "word" in code or "char" in code:
        topics.append("Strings")
    if "Counter" in code or "dict" in code or "set(" in code or "hash" in code:
        topics.append("Hash Table")
    if "binary" in code or "low <" in code or "low =" in code or "high =" in code:
        topics.append("Binary Search")
    if "Bit" in code or "|" in code or "&" in code or "^" in code or "<<" in code:
        topics.append("Bit Manipulation")
        
    if not topics:
        return "Arrays"  # default fallback
    return ", ".join(topics[:2])

def update_readme():
    readme_path = "README.md"
    existing_categories = parse_existing_categories(readme_path)
    
    problems = []
    
    # Scan current directory for problem folders
    for entry in os.scandir("."):
        if entry.is_dir() and re.match(r"^\d+-", entry.name):
            folder_name = entry.name
            problem_id = folder_name.split("-")[0]
            
            # Look for inner README.md
            inner_readme_path = os.path.join(folder_name, "README.md")
            title = folder_name.replace(problem_id + "-", "").replace("-", " ").title()
            difficulty = "Easy"
            
            if os.path.exists(inner_readme_path):
                with open(inner_readme_path, "r", encoding="utf-8") as f:
                    inner_content = f.read()
                
                # Extract title from <h2><a>...</a></h2>
                title_match = re.search(r"<h2><a [^>]*>(.*?)</a></h2>", inner_content)
                if title_match:
                    raw_title = title_match.group(1)
                    # Strip "ID. " prefix if present
                    title = re.sub(r"^\d+\.\s*", "", raw_title).strip()
                    
                # Extract difficulty from <h3>...</h3>
                diff_match = re.search(r"<h3>(.*?)</h3>", inner_content)
                if diff_match:
                    difficulty = diff_match.group(1).strip()
            
            # Find Python file
            py_file = None
            for sub_entry in os.scandir(folder_name):
                if sub_entry.is_file() and sub_entry.name.endswith(".py"):
                    py_file = sub_entry.name
                    break
            
            # Determine Category
            category = existing_categories.get(problem_id)
            if not category:
                py_path = os.path.join(folder_name, py_file) if py_file else ""
                category = guess_category(py_path)
                
            problems.append({
                "id": problem_id,
                "title": title,
                "difficulty": difficulty,
                "category": category,
                "folder": folder_name,
                "py_file": py_file
            })
            
    # Sort problems by numerical ID
    problems.sort(key=lambda x: int(x["id"]))
    
    # Generate table
    table_lines = [
        "| # | Problem | Difficulty | Category / Topics | Solution Link |",
        "| :--- | :--- | :---: | :--- | :---: |"
    ]
    
    for p in problems:
        # Format difficulty badge
        diff_lower = p["difficulty"].lower()
        if "easy" in diff_lower:
            badge = "🟢 Easy"
        elif "medium" in diff_lower:
            badge = "🟡 Medium"
        else:
            badge = "🔴 Hard"
            
        py_link = f"[Python](./{p['folder']}/{p['py_file']})" if p["py_file"] else "N/A"
        line = f"| {p['id']} | [{p['title']}](./{p['folder']}) | {badge} | {p['category']} | {py_link} |"
        table_lines.append(line)
        
    table_str = "\n".join(table_lines)
    
    # Write back to README.md
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            readme_content = f.read()
            
        new_content = re.sub(
            r"(<!-- SOLUTIONS_START -->).*?(<!-- SOLUTIONS_END -->)",
            f"\\1\n{table_str}\n\\2",
            readme_content,
            flags=re.DOTALL
        )
        
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)
            
        print(f"Successfully updated README.md with {len(problems)} solutions.")
    else:
        print("Error: README.md not found in the root directory.")

if __name__ == "__main__":
    update_readme()
