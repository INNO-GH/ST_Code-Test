/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
// Liked List + Merge Sort
// Don't forget NULL initialization!! 

// delete(deletehead) and insert(inserttail) function
struct ListNode* delete(struct ListNode* list) {
    struct ListNode* term = list->next;
    free(list);
    return term;
}
struct ListNode* insert(struct ListNode* list, int val) {
    struct ListNode* term = list;
    struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
    node->val = val;
    node->next = NULL;
    if (term == NULL) {       
        return node;
    }
    while (term->next != NULL) {
        term = term->next;
    }
    term->next = node;
    return list;
}
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode* output = NULL;
    while (1) {
	// There are 4 cases we should consider 
        if (list1 == NULL && list2 == NULL) {
            break;
        }
        else if (list1 == NULL) {
            while (list2 != NULL) {
                output = insert(output, list2->val);
                list2 = delete(list2);
            }
            break;
        }
        else if (list2 == NULL) {
            while (list1 != NULL) {
                output = insert(output, list1->val);
                list1 = delete(list1);
            }
            break;
        }
        else {
            if (list1->val <= list2->val) {
                output = insert(output, list1->val);
                list1 = delete(list1);
            }
            else {
                output = insert(output, list2->val);
                list2 = delete(list2);
            }
        }
    }
    return output;
}
