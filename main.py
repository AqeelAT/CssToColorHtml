import sys, re

with open(sys.argv[0], 'r') as file:
    css = file.read()

css = css.upper()
colors = list(set(re.findall(r'([#][A-Fa-f0-9]{3}|[#][A-Fa-f0-9]{6})[\W]', css)))
shades = list(set(re.findall(r'\d{1,3}, *\d{1,3}, *\d{1,3}, *\d+(\.\d+)?\)', css)))

new_css = ""
new_html = ""
for i in range(len(colors)):
    new_css += "\n      .color" + str(i + 1) + " {\n        background-color: " + colors[i] + ";\n      }\n"
    new_html += "\n    <div class=\"colors color" + str(i + 1) + "\"><span class=\"color-text\">" + colors[
        i] + "</span></div>\n"

js = "    <script>\n" \
     "      document.addEventListener('click', function(event) {\n" \
     "        if (!(event.target.matches('.colors') || event.target.matches('.color-text'))) return;\n" \
     "        var text = event.target.innerText;\n" \
     "        console.log(text);\n" \
     "        const el = document.createElement('textarea');\n" \
     "        document.body.appendChild(el);\n" \
     "        el.value = text;\n" \
     "        el.select();\n" \
     "        document.execCommand('copy');\n" \
     "        document.body.removeChild(el);\n" \
     "      }, false);" \
     "    </script>"

html = '<!doctype html>\n' \
       '\n' \
       '<html lang="en">\n' \
       '  <head>\n' \
       '    <meta charset="utf-8">\n' \
       '\n' \
       '    <title>The Colors</title>\n' \
       '\n' \
       '    <style>\n' \
       '      body {margin: 0;}\n\n' \
       '      .color-text {background-color: white;}\n\n' \
       '      .colors {\n' \
       '        text-align: center;\n' \
       '        line-height: 2em;\n' \
       '        height: 2em;\n' \
       '      }\n\n' \
       + new_css \
       + '    </style>\n' \
         '\n' \
         '\n' \
       + js \
       + '\n' \
         '  </head>\n' \
         '  <body>\n' \
       + new_html \
       + '  </body>\n' \
         '</html>'

with open("index.html", "w") as output:
    output.write(html)
