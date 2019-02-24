# with구문을 써서 파일을 열면 close 처리를 안해줘도 된다.
with open("foo.txt",'w') as f:
    f.write("Hellp python")
    