 #input string = "1001011"
#output = "ABACA"

def decodeHuff(root, s):
	#Enter Your Code Here
    for i in range(len(s)):
        curr = root
        if s[i] == '0':
            curr = curr.left
        elif s[i] == '1':
            curr = curr.right
        if not curr.left and not curr.right:  # if it is leaf node
            print(curr.data,end="")
            curr = root