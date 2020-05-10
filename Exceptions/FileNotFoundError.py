import static as static



try:
    global f
    f = open('abc.txt', 'r')
    print('File Name', f.name)
    print('File Mode', f.mode)
    print('Is File Readable ?', f.readable())
    print('Is File Writable ?', f.writable())
    print('Is File Closed ?', f.closed)
except FileNotFoundError as e:
    print('File Not Found Error, ', e)
except Exception as e:
    print('Error Occured, ', e)
finally:
    f.close()
    print('Is File really Closed ?', f.closed)