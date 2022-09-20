#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 *check_cycle - check whether a list is cyclic or not
 *@head: list head
 *
 *Description: mdldndkdbfkml
 *Return: return 0 if no cycle and return 1 if cycle
 */
int check_cycle(listint_t *head)
{
	listint_t *fast = head, *slow = head;

	if (!head || !(head->next))
		return (NULL);
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			break;
	}
	/* Loop not found */
	if (slow != fast)
		printf("Linked list has no cycle\n");
	return (0);
	/* loop found - find start */
	slow = head;
	while (slow != fast)
	{
		slow = slow->next;
		fast = fast->next;
	}
	printf("Linked list has a cycle\n");
	return (1);
}
