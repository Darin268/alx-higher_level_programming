#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - To check if palindrome or not
 * @head: head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux_palindrome(head, *head));
}

/**
 * aux_palindrome - To know if it is plaindrome
 * @head: head of the list
 * @end: end of the list
 */
int aux_palindrome(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (aux_palindrome(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)-> next;
		return (1);
	}

	return (0);
}
