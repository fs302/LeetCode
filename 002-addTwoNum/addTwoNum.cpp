/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

#include <iostream>
using namespace std;

struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int stack = 0;
        ListNode *result = new ListNode(0), *cur = 0;

        if (l1 != NULL && l2 != NULL) {
        	int digit = l1->val + l2->val + stack;
        	stack = digit >= 10 ? 1 : 0;
        	digit = digit >= 10 ? digit - 10 : digit;
        	result->val = digit;
        	cur = result;
        	l1 = l1->next;
        	l2 = l2->next;
        }

        while(l1 != NULL || l2 != NULL) {
        	int digit = stack + (l1 != NULL ? l1->val : 0) + (l2 != NULL ? l2->val : 0);
        	stack = digit >= 10 ? 1 : 0;
        	digit = digit >= 10 ? digit - 10 : digit;
        	ListNode *p = new ListNode(0);
        	p->val = digit;
        	cur->next = p;
        	cur = p;
        	l1 = l1 != NULL ? l1->next : NULL;
        	l2 = l2 != NULL ? l2->next : NULL;
        }

        if (stack > 0){
        	ListNode *p = new ListNode(0);
        	p->val = stack;
        	cur->next = p;
        	cur = p;
        }
        return result;
    }
};

ListNode* makeNum(int num) {
	ListNode *result = 0, *cur = 0;
	if (num == 0) {
		return new ListNode(0);
	}
	while(num > 0) {
		ListNode *p = new ListNode(0);
		p->val = num % 10;
		num = num / 10;
		if (result == NULL) {
			cur = p;
			result = cur;
		} else {
			cur->next = p;
			cur = p;
		}
	}
	return result;
}

void printNode(ListNode* c) {
	while (c != NULL) {
		cout << c->val << endl;
		c = c->next;
	}
	cout << endl;
}

int main() {
	ListNode *a = 0, *b = 0, *c = 0;
	Solution s;
	a = makeNum(9);
	b = makeNum(999999991);
	c = s.addTwoNumbers(a, b);
	printNode(c);
	return 0;
}