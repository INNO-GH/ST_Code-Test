// Just use existing linked list directly

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    struct ListNode reslist;
    struct ListNode *res=&reslist;
    if(list1==NULL) // If one of list is NULL
        return list2;
    if(list2==NULL)
        return list1;
    while(list1!=NULL && list2!= NULL)
    {
        if(list1->val<=list2->val)
        {
            res->next=list1; // give node from list to res
            list1=list1->next;
        }
        else
        {
            res->next=list2;
            list2=list2->next;
        }
        res=res->next;
    }
    if(list1==NULL && list2 != NULL){ // When one of list is empty -> Just bring another node
        res->next=list2;
    }
    else if(list2==NULL && list1 != NULL){
        res->next=list1;
    }
    return reslist.next;
}
