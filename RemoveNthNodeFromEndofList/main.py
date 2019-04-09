def removeNthFromEnd(head, n):
    pn=head
    while n>1:
        pn=pn.next
        n-=1
    if pn.next is None:#如果是倒数第length个
        return head.next
    pn=pn.next#让pn向后走1个
    p=head
    while pn.next!=None:
        p=p.next
        pn=pn.next
    invalidNode=p.next#待删除的节点
    p.next=invalidNode.next

    return head
