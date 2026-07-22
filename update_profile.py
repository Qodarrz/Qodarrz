import re

def update_profile(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    new_profile = '''<text x="390" y="30" fill="#c9d1d9">
<tspan x="390" y="30">xroot@HeiDarrz</tspan> -——————————————————————————————————————————-—-
<tspan x="390" y="50" class="cc">. </tspan><tspan class="key">Role</tspan>:<tspan class="cc"> ...................... </tspan><tspan class="value">Software, IoT, CyberSec</tspan>
<tspan x="390" y="90" class="cc">. </tspan><tspan class="key">Location</tspan>:<tspan class="cc"> .................. </tspan><tspan class="value">Bogor City, West Java, ID</tspan>
<tspan x="390" y="110" class="cc">. </tspan><tspan class="key">Education</tspan>:<tspan class="cc"> ................. </tspan><tspan class="value">SMKN 4 Bogor City</tspan>
<tspan x="390" y="130" class="cc">. </tspan>
<tspan x="390" y="150" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Programming</tspan>:<tspan class="cc"> ..... </tspan><tspan class="value">TypeScript, Golang, Python</tspan>
<tspan x="390" y="170" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Markup</tspan>:<tspan class="cc"> .......... </tspan><tspan class="value">HTML, CSS, JSON, YAML</tspan>
<tspan x="390" y="190" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Spoken</tspan>:<tspan class="cc"> .......... </tspan><tspan class="value">Indonesian, English</tspan>
<tspan x="390" y="210" class="cc">. </tspan>
<tspan x="390" y="230" class="cc">. </tspan><tspan class="key">TechStack</tspan>.<tspan class="key">Frameworks</tspan>:<tspan class="cc"> ...... </tspan><tspan class="value">Next.js, FastAPI, Flutter</tspan>
<tspan x="390" y="250" class="cc">. </tspan><tspan class="key">TechStack</tspan>.<tspan class="key">Backend</tspan>:<tspan class="cc"> ......... </tspan><tspan class="value">ExpressJS, Gin, NestJS</tspan>
<tspan x="390" y="270" class="cc">. </tspan><tspan class="key">TechStack</tspan>.<tspan class="key">Tools</tspan>:<tspan class="cc"> ........... </tspan><tspan class="value">TensorFlow, OpenCV, n8n</tspan>
<tspan x="390" y="290" class="cc">. </tspan>
<tspan x="390" y="310" class="cc">. </tspan><tspan class="key">OS</tspan>.<tspan class="key">Mobile</tspan>:<tspan class="cc"> ................. </tspan><tspan class="value">LineageOS, GrapheneOS, CalyxOS</tspan>
<tspan x="390" y="330" class="cc">. </tspan><tspan class="key">OS</tspan>.<tspan class="key">Desktop</tspan>:<tspan class="cc"> ................ </tspan><tspan class="value">Ubuntu, Mint, Windows, Arch</tspan>
<tspan x="390" y="350" class="cc">. </tspan>
<tspan x="390" y="370" class="cc">. </tspan><tspan class="key">Expertise</tspan>.<tspan class="key">Domain</tspan>:<tspan class="cc"> .......... </tspan><tspan class="value">Web, App, IoT, Cybersecurity</tspan>
<tspan x="390" y="390" class="cc">. </tspan><tspan class="key">Expertise</tspan>.<tspan class="key">SoftSkills</tspan>:<tspan class="cc"> ...... </tspan><tspan class="value">Teamwork, Problem Solving</tspan>
<tspan x="390" y="410" class="cc">. </tspan>
<tspan x="390" y="430" class="cc">. </tspan><tspan class="key">Hobbies</tspan>.<tspan class="key">Hardware</tspan>:<tspan class="cc"> .......... </tspan><tspan class="value">Custom OS, IoT Prototyping</tspan>
<tspan x="390" y="450" class="cc">. </tspan><tspan class="key">Hobbies</tspan>.<tspan class="key">Software</tspan>:<tspan class="cc"> .......... </tspan><tspan class="value">Web Dev, Apps, Bug Bounty</tspan>
<tspan x="390" y="470" class="cc">. </tspan>
<tspan x="390" y="490" class="cc">- </tspan><tspan>Contact</tspan> -——————————————————————————————————————————————-—-
<tspan x="390" y="510" class="cc">. </tspan><tspan class="key">Email</tspan>:<tspan class="cc"> ..................... </tspan><tspan class="value">heidararizki@gmail.com</tspan>
<tspan x="390" y="550" class="cc">. </tspan><tspan class="key">LinkedIn</tspan>:<tspan class="cc"> .................. </tspan><tspan class="value">in/muhammadheidararrizqie</tspan>
<tspan x="390" y="570" class="cc">. </tspan><tspan class="key">Portfolio</tspan>:<tspan class="cc"> ................. </tspan><tspan class="value">https://heidar.my.id</tspan>
<tspan x="390" y="590" class="cc">. </tspan><tspan class="key">GitHub</tspan>:<tspan class="cc"> .................... </tspan><tspan class="value">Qodarrz</tspan>
<tspan x="390" y="610" class="cc">. </tspan>
<tspan x="390" y="630" class="cc">- </tspan><tspan>GitHub Stats</tspan> -—————————————————————————————————————————-—-
<tspan x="390" y="650" class="cc">. </tspan><tspan class="key">Repos</tspan>:<tspan class="cc" id="repo_data_dots"> .... </tspan><tspan class="value" id="repo_data">95</tspan> {<tspan class="key">Contributed</tspan>: <tspan class="value" id="contrib_data">133</tspan>} | <tspan class="key">Stars</tspan>:<tspan class="cc" id="star_data_dots"> ........... </tspan><tspan class="value" id="star_data">342</tspan>
<tspan x="390" y="670" class="cc">. </tspan><tspan class="key">Commits</tspan>:<tspan class="cc" id="commit_data_dots"> .................. </tspan><tspan class="value" id="commit_data">2,116</tspan> | <tspan class="key">Followers</tspan>:<tspan class="cc" id="follower_data_dots"> ....... </tspan><tspan class="value" id="follower_data">196</tspan>
<tspan x="390" y="690" class="cc">. </tspan><tspan class="key">Lines of Code on GitHub</tspan>:<tspan class="cc" id="loc_data_dots">. </tspan><tspan class="value" id="loc_data">446,276</tspan> ( <tspan class="addColor" id="loc_add">523,178</tspan><tspan class="addColor">++</tspan>, <tspan id="loc_del_dots"> </tspan><tspan class="delColor" id="loc_del">76,902</tspan><tspan class="delColor">--</tspan> )
</text>'''

    # Update profile text block
    pattern = re.compile(r'<text x="390" y="30".*?</text>', re.DOTALL)
    new_content = pattern.sub(new_profile, content)
    
    # Update height in <svg> tag
    new_content = re.sub(r'<svg(.*?)height="(?:530|680)px"', r'<svg\1height="720px"', new_content)
    # Update height in <rect> tag
    new_content = re.sub(r'<rect(.*?)height="(?:530|680)px"', r'<rect\1height="720px"', new_content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Patched profile data in {filename}")

if __name__ == '__main__':
    update_profile('dark_mode.svg')
    update_profile('light_mode.svg')
