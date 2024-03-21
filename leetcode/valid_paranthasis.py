def isValid( s: str) -> bool:
    st = []
    for c in s:
        if c in ['(', '[', '{']:
            st.append(c)
        elif len(st) > 0 and c == ')':
            if st[-1] != '(':
                return False
            st.pop()
        elif len(st) > 0 and c == ']':
            if st[-1] != '[':
                return False
            st.pop()
        elif len(st) > 0 and c == '}':
            if st[-1] != '{':
                return False
            st.pop()
    print(st)

isValid("()[]{}")