#include "lists.h"

/**
 * is_palindrome - To check of list is plindrome
 * @head: head of list
 * Return: 0 if it is not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (check_plaindrome(head, *head));
}

/**
 * check_plaindrome - To check if the list if palindrome
 * @head: head of list
 * @end: end of list
 * Return: 0 if not palindrome and 1 if it is
 */

int check_plaindrome(listint_t **head, listint_t *end)
{
	if (last == NULL)
		return (1);
	if (check_plaindrome(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
