with open('build_portal.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = '</footer>'
if target in text:
    # replace first occurrence after <main>
    main_pos = text.find('</main>')
    foot_pos = text.find('</footer>', main_pos)
    if foot_pos != -1:
        new_text = text[:foot_pos+9] + '\n  </div><!-- End #app-container -->\n' + text[foot_pos+9:]
        with open('build_portal.py', 'w', encoding='utf-8') as f:
            f.write(new_text)
        print("Successfully closed #app-container after </footer>!")
    else:
        print("</footer> after </main> not found!")
else:
    print("</footer> not found!")
