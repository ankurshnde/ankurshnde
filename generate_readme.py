import os

def make_line(left_part, visual_center, right_border=" |", width=80, html_center=None):
    center_text = html_center if html_center is not None else visual_center
    visual_len = len(left_part) + len(visual_center) + len(right_border)
    spaces_needed = width - visual_len
    return f"{left_part}{center_text}" + " " * spaces_needed + right_border

def generate():
    width = 80
    border_top_bottom = "+" + "-" * (width - 2) + "+"
    border_middle = "+" + "-" * (width - 2) + "+"

    lines = []
    lines.append('<img src="assets/banner.png" width="100%" alt="Ankur Shinde Desktop Mockup">')
    lines.append('')
    lines.append('<div align="center">')
    lines.append('<pre>')
    lines.append(border_top_bottom)
    
    # Header block
    lines.append(make_line("| ", "C:\\Users\\Ankur> whoami"))
    lines.append(make_line("| ", "ankur.exe [AI Engineer & Builder]"))
    lines.append(border_middle)
    
    # dir block header
    lines.append(make_line("| ", "C:\\Users\\Ankur> dir /b"))
    
    # Empty line
    lines.append(make_line("|", "", right_border="|"))
    
    # Directory contents
    links = [
        ("[DIR]", "Publications", "https://ankurshinde.vercel.app/publications"),
        ("[DIR]", "Research/Articles", "https://ankurshinde.vercel.app/articles"),
        ("[URL]", "LinkedIn.url", "https://www.linkedin.com/in/ankurshinde/"),
        ("[URL]", "X.url", "https://x.com/ankurshn"),
        ("[URL]", "Portfolio.url", "https://ankurshinde.vercel.app/"),
        ("[URL]", "Contact.url", "mailto:ankurshinde.dev@gmail.com")
    ]
    
    for prefix, name, url in links:
        left_part = f"|  {prefix}  "
        html_link = f'<a href="{url}">{name}</a>'
        lines.append(make_line(left_part, name, html_center=html_link))
        
    # Empty line
    lines.append(make_line("|", "", right_border="|"))
    lines.append(border_top_bottom)
    lines.append('</pre>')
    lines.append('</div>')
    lines.append('')
    
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("README.md generated successfully with perfect alignment!")

if __name__ == "__main__":
    generate()
