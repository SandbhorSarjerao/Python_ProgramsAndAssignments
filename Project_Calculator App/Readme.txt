
1) KIVI Library => pip install kivy==2.2.1
   https://kivy.org/
   Open Source Python App Development Framework.

   Build and distribute beautiful Python cross-platform GUI apps with ease.
   Kivy runs on Android, iOS, Linux, macOS and Windows.

   With a single codebase, you will be able to deploy apps on Windows, Linux, macOS, iOS and Android.

2) Buildozer => pip install --user --upgrade buildozer
   https://buildozer.readthedocs.io/en/latest/installation.html
   https://buildozer.readthedocs.io
   Used buildozer to convert python script.

3) Cython => pip install cython==0.29.19

4) google colab => Kivy App To APK =>
   https://colab.research.google.com/drive/1b9gMzs6XAtxCtahxei4N0fWZk7xiPlVw?usp=sharing

   From Google Colab website above link install/run commands ==>
   a) install buildozer
   b) install cython==0.29.21
   c) install
      sudo apt-get install -y \
        ... python3-pip \
        ... build-essential \
        ... git \
        ... python3 \
        ... python3-dev \
        ... ffmpeg \
        ... libsdl2-dev \
        ... libsdl2-image-dev \
        ... libsdl2-mixer-dev \
        ... libsdl2-ttf-dev \
        ... libportmidi-dev \
        ... libswscale-dev \
        ... libavformat-dev \
        ... libavcodec-dev \
        ... zlib1g-dev

   d) install
      sudo apt-get install -y \
        ... libgstreamer1.0 \
        ... gstreamer1.0-plugins-base \
        ... gstreamer1.0-plugins-good

   e) install
      sudo apt-get install build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev zlib1g-dev libssl-dev openssl libgdbm-dev libgdbm-compat-dev liblzma-dev libreadline-dev libncursesw5-dev libffi-dev uuid-dev libffi7

   f) install
      sudo apt-get install libffi-dev

   g) run command
      buildozer init
      *** Press y for continue
      *** Refresh left-side files pane
      *** Verify "buildozer.spec" is got created

    h) From the local project folder copy below to files and paste it in left-side files pane
       -- calculator.png
       -- calculatorsplash.png

    i) Open "buildozer.spec" file , and updated below lines
       - line-4  => title = Calculator By Sarjerao
       - line-40 => requirements = python3,kivy==2.2.1,kivymd,pillow
       - line-47 => #presplash.filename = %(source.dir)s/data/presplash.png
                   Remove Comment (#)
                   presplash.filename = %(source.dir)s/calculatorsplash.png
       - line-50 => #icon.filename = %(source.dir)s/data/icon.png
                    Remove Comment (#)
                    icon.filename = %(source.dir)s/calculator.png
       close "buildozer.spec" file

    j) From the local project folder copy below to files and paste it in left-side files pane
       -- main.py

    k) run command and wait for 15 mins
       buildozer -v android debug
       *** Press y for continue
       *** Refresh left-side files pane
       *** Verify "" APK is got created



