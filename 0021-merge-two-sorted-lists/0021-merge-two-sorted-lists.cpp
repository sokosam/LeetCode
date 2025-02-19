/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        
        ListNode* ans = NULL;
        ListNode* head = NULL;
        while (list1 && list2){
            if (list1->val <= list2->val){
                if (!head){
                    head = list1;
                    ans = head;
                    list1 = list1 -> next;
                }
                else{
                    head->next = list1;
                    list1 = list1 -> next;
                    head = head->next;
                }
            }
            else{
                if (!head){
                    head = list2;
                    ans = head;
                    list2 = list2 -> next;
                }
                else{
                    head->next = list2;
                    list2 = list2 -> next;
                    head = head->next;
            }
        }}
        if (list1){
            if (!head){
                return list1;
            }
            else{
                head->next = list1;
            }
        }
        if (list2){
            if (!head){
                return list2;
            }
            else{
                head->next = list2;
            }
        }

        return ans;

    }
};