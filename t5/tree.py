import random

class Node():
    def __init__(self,val):
        self.val = val
        self.parent:Node = None
        self.left:Node = None
        self.right:Node = None
        self.color = 1 # 0 - черный 1 - красный
    
    @property
    def grandparent(self):
        if self.parent != None:
            return self.parent.parent

    @property
    def uncle(self):
        g = self.grandparent
        if g is None:
            return None
        if self.parent == g.left:
            return g.right
        return g.left

    @property
    def sibling(self):
        if self == self.parent.left:
            return self.parent.right
        return self.parent.left

    def __repr__(self) -> str:
        return f"{self.val}:{'R' if self.color == 1 else 'B'}"
        

class RedBlackTree():
    def __init__(self):
        self.NULL = Node ( 0 )
        self.root = self.NULL


    def insert_node(self, key):
        node = Node(key)
        node.parent = None
        node.val = key
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1

        y = None
        x = self.root

        while x != self.NULL :                           # ищем позицию для вставки
            y = x
            if node.val < x.val :
                x = x.left
            else :
                x = x.right

        node.parent = y
        if y == None :                                   # если родителя нет, значит это корень
            self.root = node
        elif node.val < y.val:
            y.left = node
        else :
            y.right = node
        self._fix_insert(node)                         # восстанавливаем дерево
        return node


    def minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node


    # левый поворот
    def _left_rotate ( self , x ) :
        y = x.right                                      
        x.right = y.left
        if y.left != self.NULL :
            y.left.parent = x

        y.parent = x.parent                              
        if x.parent == None :                            
            self.root = y
        elif x == x.parent.left :
            x.parent.left = y
        else :
            x.parent.right = y
        y.left = x
        x.parent = y


    # правый поворот
    def _right_rotate ( self , x ) :
        y = x.left                                       
        x.left = y.right                                 
        if y.right != self.NULL :
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None :                            
            self.root = y                                
        elif x == x.parent.right :
            x.parent.right = y
        else :
            x.parent.left = y
        y.right = x
        x.parent = y

    def _fix_insert(self, n:Node):
        self._insert_case1(n)
    
    def _insert_case1(self, n: Node):
        # Текущий узел является корнем. В этом случае, он перекрашивается в чёрный цвет, чтобы оставить верным Свойство Корень — чёрный. Так как это действие добавляет один чёрный узел в каждый путь, Свойство Все пути от любого данного узла до листовых узлов содержат одинаковое число чёрных узлов) не нарушается.
        if n.parent == None:
            n.color = 0
            return
        self._insert_case2(n)
    
    def _insert_case2(self, n: Node):
        # Предок текущего узла чёрный, то есть Свойство Оба потомка каждого красного узла — чёрные не нарушается. 
        # В этом случае дерево остаётся корректным. 
        # Свойство Все пути от любого данного узла до листовых узлов содержат одинаковое число чёрных узлов) не нарушается, потому что текущий узел N имеет двух чёрных листовых потомков, но так как N является красным, путь до каждого из этих потомков содержит такое же число чёрных узлов, что и путь до чёрного листа, который был заменен текущим узлом, так что свойство остается верным. 
        if n.parent.color == 0:
            return
        self._insert_case3(n)
    
    def _insert_case3(self, n: Node):
        #Если и родитель и дядя — красные, то они оба могут быть перекрашены в чёрный, и дедушка станет красным (для сохранения свойства Все пути от любого данного узла до листовых узлов содержат одинаковое число чёрных узлов). 
        # Теперь у текущего красного узла N чёрный родитель. 
        # Так как любой путь через родителя или дядю должен проходить через дедушку, число чёрных узлов в этих путях не изменится. 
        # Однако, дедушка теперь может нарушить свойства (Корень — чёрный) или (Оба потомка каждого красного узла — чёрные) (свойство может быть нарушено, так как родитель G может быть красным). 
        # Чтобы это исправить, операция повторяется для дедушки начиная с 1 случая. 
        u = n.uncle
        if u.color is not None and u.color == 1:
            n.parent.color = 0
            u.color = 0
            g = n.grandparent
            g.color = 1
            self._insert_case1(g)
        else:
            self._insert_case4(n)
    
    def _insert_case4(self, n:Node):
        # Родитель является красным, но дядя — чёрный. Также, текущий узел  правый потомок отца, а отец в свою очередь — левый потомок своего отца. 
        # В этом случае может быть произведен поворот дерева, который меняет роли текущего узла и его отца. 
        # Тогда, для бывшего отца в обновленной структуре используем случай 5, потому что Свойство (Оба потомка любого красного узла — чёрные) все ещё нарушено. 
        # Вращение приводит к тому, что некоторые пути проходят через текцщий узел, чего не было до этого. 
        # Это также приводит к тому, что некоторые пути не проходят через родителя. 
        # Однако, оба эти узла являются красными, так что Свойство (Все пути от любого данного узла до листовых узлов содержат одинаковое число чёрных узлов) не нарушается при вращении. Однако Свойство (Оба потомка каждого красного узла — чёрные) всё ещё нарушается, но теперь задача сводится к Случаю 5. 
        g = n.grandparent
        if n == n.parent.right and n.parent == g.left:
            self._left_rotate(n.parent)
            n = n.left
        elif n == n.parent.left and n.parent == g.right:
            self._right_rotate(n.parent)
            n = n.right
        self._insert_case5(n)
    
    def _insert_case5(self, n:Node):
        # Родитель является красным, но дядя чёрный, текущий узел — левый потомок отца и отец — левый потомок. 
        # В этом случае выполняется поворот дерева на G. В результате получается дерево, в котором бывший родитель теперь является родителем и текущего узла и бывшего дедушки. Известно, что дедушка чёрный, 
        # так как его бывший потомок не мог бы в противном случае быть красным. Тогда цвета родителя и дедушки меняются и в результате дерево удовлетворяет Свойству (Оба потомка любого красного узла — чёрные). 
        # Свойство (Все пути от любого данного узла до листовых узлов содержат одинаковое число чёрных узлов) также остается верным, так как все пути, 
        # которые проходят через любой из этих трех узлов, ранее проходили через дедушку, поэтому теперь они все проходят через родителя. 
        # В каждом случае, из этих трёх узлов только один окрашен в чёрный.
        g = n.grandparent
        n.parent.color = 0
        g.color = 1
        if n == n.parent.left and n.parent == g.left:
            self._right_rotate(g)
        else:
            self._left_rotate(g)


    def delete_node(self, key):
        z = self.NULL
        n = self.root

        while n != self.NULL:
            if n.val == key:
                z = n
 
            if n.val <= key:
                n = n.right
            else:
                n = n.left
        
        if z == self.NULL:
            raise KeyError("не удалось найти узел с таким значением")
        
        if z.left == self.NULL or z.right == self.NULL:
            y = z
        else:
            y = z.right
            while y.left != self.NULL:
                y = y.left
        
        if y.left != self.NULL:
            x = y.left
        else:
            x = y.right
        
        x.parent = y.parent
        if y.parent != self.NULL:
            if y == y.parent.left:
                y.parent.left = x
            else:
                y.parent.right = x
        else:
            self.root = x
        if y != z:
            z.val = y.val
        if y.color == 0:
            self._delete_case1(x)


    def _delete_case1(self, n:Node):
        """N — новый корень. В этом случае, все сделано. 
        Мы удалили один чёрный узел из каждого пути и новый корень является чёрным узлом, так что свойства сохранены. """
        if n.parent != self.NULL:
            self._delete_case2(n)
    
    def _delete_case2(self, n:Node):
        """ брат — красный. В этом случае мы меняем цвета отца и брата, и затем делаем вращение 
            влево вокруг отца, ставя брат дедушкой узла. Нужно заметить, что отец должен быть чёрным,
            если он имеет красного потомка. Результирующее поддерево всё равно имеет черных
            узлов на единицу меньше, поэтому на этом мы ещё не закончили. 
            Теперь узел имеет чёрного брата и красного отца, поэтому мы можем перейти к шагу 4, 5 или 6. 
            (Его новый брат является чёрным потому, что он был потомком красного брат"""
        s = n.sibling
        if s.color == 1:
            n.parent.color = 1
            s.color = 0
            if n == n.parent.left:
                self._left_rotate(n.parent)
            else:
                self._right_rotate(n.parent)
        self._delete_case3(n)
    
    def _delete_case3(self, n:Node):
        """отец, брат, и дети брата — чёрные. В этом случае мы просто перекрашиваем брата в красный. 
        В результате все пути, проходящие через брата, но не проходящие через узел, имеют на один чёрный 
        узел меньше. Так как удаление отца приводит к тому, что все пути, проходящие через узел, 
        содержат на один чёрный узел меньше, то такие действия выравнивают баланс. 
        Тем не менее, все проходящие через отца пути теперь содержат на один чёрный узел меньше, 
        чем пути, которые через отца не проходят, поэтому свойство (все пути из любой вершины к её 
        листовым узлам содержат одинаковое количество чёрных узлов) все ещё нарушено. 
        Чтобы это исправить, мы применяем процедуру перебалансировки к отцу, начиная со случая 1. """
        s = n.sibling
        if n.parent.color == 0 and s.color == 0 and s.left.color == 0 and s.right.color == 0:
            s.color = 1
            self._delete_case1(n.parent)
        else:
            self._delete_case4(n)
    
    def _delete_case4(self, n:Node):
        """брат и его дети — чёрные, но отец — красный. В этом случае мы просто меняем цвета брата и отца. 
        Это не влияет на количество чёрных узлов на путях, проходящих через брата, 
        но добавит один к числу чёрных узлов на путях, проходящих через узел, восстанавливая 
        тем самым влияние удаленного чёрного узла. """
        s = n.sibling
        if n.parent.color == 1 and s.left.color == 0 and s.right.color == 0 and s.color == 0:
            s.color = 1
            n.parent.color = 0
        else:
            self._delete_case5(n)
    
    def _delete_case5(self, n:Node):
        """брат — чёрный, левый потомок брата — красный, правый потомок брата — чёрный, и узел является левым потомков своего отца. В этом случае мы вращаем дерево вправо вокруг брата. Таким образом левый потомок брата становится его отцом и новым братом узла. После этого мы меняем цвета у брата и его нового отца. Все пути по-прежнему содержат одинаковое количество чёрных узлов, но теперь у узла есть чёрный брат с красным правым потомком, и мы переходим к случаю 6. Ни узел, ни его отец не влияют на эту трансформацию. """
        s = n.sibling
        if s.color == 0:
            if n == n.parent.left and s.right.color == 0 and s.left.color == 1:
                s.color = 1
                s.left.color = 0
                self._right_rotate(s)
            elif n == n.parent.right and s.left.color == 0 and s.right.color == 1:
                s.color = 1
                s.right.color = 0
                self._left_rotate(s)
        self._delete_case6(n)

    def _delete_case6(self, n:Node):
        s = n.sibling
        s.color = n.parent.color
        n.parent.color = 0
        if n == n.parent.left:
            s.right.color = 0
            self._left_rotate(n.parent)
        else:
            s.left.color = 0
            self._right_rotate(n.parent)
    
    def print(self):
        self._traverse_print(self.root, "")

    def _traverse_print(self, node:Node, path):
        if node is not None and node is not self.NULL:
            print(f"{path} - {node}", end=",")
            self._traverse_print(node.left, path + "0")
            self._traverse_print(node.right, path + "1")


if __name__ == "__main__":
    tree = RedBlackTree()
    data = set(random.randint(-10, 10) for _ in range(0, 15))
    print("исходные данные:", *data)
    for e in data:
        tree.insert_node(e)
    print("полученное дерево")
    tree.print()
    print()
    while True:
        match input("введите 1 для добавления, 0 для удаления узла:"):
            case "1":
                print(tree.insert_node(int(input("введите значение для вставки:"))))
                tree.print()
                print()
            case "0":
                tree.delete_node(int(input("введите узел для удаления:")))
                tree.print()
                print()
            case _:
                break