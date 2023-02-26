class TextNode:
    __slots__ = ('value', 'prev', 'next')

    def __init__(self, value=None, prev=None, nxt=None):
        self.value = value
        self.next = nxt
        self.prev = prev

class Cursor:
    __slots__ = ('prev', 'next')
    def __init__(self, prev=None, nxt=None):
        self.prev = prev
        self.next = nxt

    def move_right(self):
        if self.next:
            self.prev = self.next
            self.next = self.next.next

    def move_left(self):
        if self.prev:
            self.next = self.prev
            self.prev = self.prev.prev

    def add_node(self, node):
        self.prev.next = node
        node.prev = self.prev
        if self.next:
            node.next = self.next
            self.next.prev = node
        self.prev = node

    def remove_left(self):
        if self.prev and self.prev.prev:
            to_delete = self.prev
            self.prev = self.prev.prev
            self.prev.next = self.next
            if self.next:
                self.next.prev = self.prev
            del to_delete
        elif not self.prev.prev:
            if self.next:
                self.next.prev = None
            del self.prev
            self.prev = None


class TextEditor:

    def __init__(self):
        self.cursor = Cursor()

    def addText(self, text: str) -> None:
        for c in text:
            if self.cursor.prev:
                self.cursor.add_node(TextNode(c, self.cursor.next))
            else:
                self.cursor.prev = TextNode(c)

    def deleteText(self, k: int) -> int:
        count = 0
        while count < k and self.cursor.prev:
            self.cursor.remove_left()
            count += 1
        return count

    def _return_text(self):
        text = ''
        if not self.cursor.prev:
            return text
        node = self.cursor.prev
        while len(text) < 10:
            text += node.value
            node = node.prev
            if not node or not node.prev:
                if node and len(text) < 10:
                    text += node.value
                break
        return text[::-1]

    def cursorLeft(self, k: int) -> str:
        while k and self.cursor.prev:
            self.cursor.move_left()
            k -= 1
        return self._return_text()

    def cursorRight(self, k: int) -> str:
        while k and self.cursor.next:
            self.cursor.move_right()
            k -= 1
        return self._return_text()


if __name__ == '__main__':
    # te = TextEditor()
    # te.addText('leetcode')
    # te.print()
    # print()
    # print(te.deleteText(4))
    # te.print()
    # print()
    # te.addText('practice')
    # te.print()
    # print()
    # print(te.cursorRight(3))
    # print(te.cursorLeft(8))
    # print(te.deleteText(10))
    # print(te.cursorLeft(2))
    # print(te.cursorRight(6))
    # rr = te.cursorRight(2)
    # print

    t = TextEditor()
    commands = ["cursorLeft","cursorRight","addText","deleteText","addText","cursorRight","cursorLeft","deleteText","addText","cursorRight","cursorLeft","cursorLeft","addText","addText","addText","addText","addText","addText","cursorRight","cursorLeft","addText","cursorLeft","deleteText","addText","cursorLeft","deleteText","cursorRight","cursorRight","cursorRight","cursorRight","cursorRight","deleteText","deleteText","cursorRight","cursorRight","addText","addText","cursorRight","addText","cursorLeft","addText","cursorLeft","addText","cursorLeft","cursorLeft","addText","cursorLeft","addText","addText","deleteText","cursorLeft","cursorLeft","addText","cursorRight","addText","cursorRight","cursorLeft","deleteText","addText","deleteText","addText","deleteText","addText","cursorRight","cursorRight","cursorRight","cursorRight","cursorRight","addText","addText","addText","addText","deleteText","cursorRight","deleteText","deleteText","deleteText","addText","cursorRight","cursorLeft","addText","cursorRight","addText","deleteText","addText","addText","cursorRight","addText","addText","addText","addText"]
    args = [[8],[16],["bgjywfocipyezop"],[4],["xptqahzitnabjfknymj"],[3],[8],[14],["ybhykj"],[20],[11],[6],["cgvuciehpswbs"],["qbnltoyeljrkknuwnxk"],["id"],["iqzpldmtqibzqesl"],["rjdhawrd"],["hqksvjqbtohltzdcw"],[17],[11],["jezisodqw"],[18],[4],["hiqvfqr"],[8],[20],[6],[16],[18],[14],[18],[18],[1],[11],[17],["ioo"],["bjpv"],[7],["cdcvaumpcexhmkzybpz"],[4],["dzghk"],[5],["iau"],[2],[19],["akijlylir"],[5],["keqeitxzcglzjixazz"],["pfypcpoqsf"],[12],[9],[11],["pr"],[2],["ystzfwtbnyhry"],[13],[17],[4],["adzaxhjh"],[14],["hnk"],[4],["zzmdfxukdiruklhviph"],[13],[11],[9],[20],[12],["pwnksifks"],["eiixxdfqcckvn"],["royfbqdzbzt"],["qjkwryvdbloilojst"],[5],[2],[5],[14],[8],["mquc"],[2],[20],["khvrtzolbgjfldu"],[5],["jszprkqstmnolvzfjf"],[8],["oeo"],["llpvbpevgvokbobqrfa"],[3],["pymdvpgisid"],["iucrbwwhhxshuxvtbrx"],["fl"],["v"]]
    expected = ["","",None,4,None,"nabjfknymj","ptqahzitna",14,None,"kjbjfknymj","gjywfocybh","bgjyw",None,None,None,None,None,None,"kjbjfknymj","zdcwfocybh",None,"vjqbtohltz",4,None,"dhqksvjqbt",20,"ibzqohiqvf","ocybhjezis","kjbjfknymj","kjbjfknymj","kjbjfknymj",18,1,"dcwfocybhj","dcwfocybhj",None,None,"bhjioobjpv",None,"umpcexhmkz",None,"umpcexhmkz",None,"mpcexhmkzi","ocybhjioob",None,"hjioobakij",None,None,12,"kijkeqeitx","ocybhjioob",None,"hjioobprak",None,"eqeitxzcgl","kystzfwtbn",4,None,14,None,4,None,"yijkeqeitx","cglzjixaly","ylirjpvcdc","kziaudzghk","udzghkybpz",None,None,None,None,5,"kwryvdbloi",5,14,8,None,"xxdfqcmquc","zghkybpzpw",None,"jfldunksif",None,8,None,None,"bobqrfakse",None,None,None,None]
    import time
    start = time.time()
    for method, arg, res in zip(commands, args, expected):
        getattr(t, method)(arg[0])
    print(time.time() - start)
