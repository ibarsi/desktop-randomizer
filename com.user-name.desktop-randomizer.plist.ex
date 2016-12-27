 <?xml version="1.0" encoding="UTF-8"?>
 <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.  dtd">
 <plist version="1.0">
 <dict>
     <key>Desktop Randomizer</key>
     <string>com.{{user-name}}.desktop-randomizer</string>

    <key>EnvironmentVariables</key>
    <dict>
         <key>PYTHONPATH</key>
         <string>/Users/{{user-name}}/Projects/desktop-randomizer/desktop-randomizer/lib/python2.7/site-packages</string>
     </dict>

     <key>ProgramArguments</key>
     <array>
         <string>/usr/local/bin/python2.7</string>
         <string>/Users/{{user-name}}/Projects/desktop-randomizer/main.py</string>
     </array>

     <key>KeepAlive</key>
     <false/>

     <key>RunAtLoad</key>
     <true/>

     <key>StartCalendarInterval</key>
     <dict>
         <key>Hour</key>
         <integer>00</integer>
         <key>Minute</key>
         <integer>00</integer>
     </dict>

     <key>StandardErrorPath</key>
     <string>/tmp/com.{{user-name}}.desktop-randomizer.err</string>
 </dict>
 </plist>