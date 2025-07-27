#include <iostream>

using namespace std;

// Node: to store the information about an element of the list
struct Node
{
    int data;
    Node* next;
};

// Head of the list
Node* head = nullptr;

// Inserting the element at any position
void insert(int data, int position)
{
    Node* temp1 = new Node();
    temp1->data = data;
    temp1->next = nullptr;

    if (position == 1)
    {
        temp1->next = head;
        head = temp1;
        return;
    }
    
    Node* temp2 = head;
    for (int i = 0; i < position - 2; i++) 
    {
        if (temp2 == nullptr) 
        {
            cout << "Invalid position\n";
            return;
        }
        temp2 = temp2->next;
    }

    temp1->next = temp2->next;
    temp2->next = temp1;
}

// Deleting the list element at any position
void Delete(int position)
{
    // if list is empty
    if (head == nullptr) {
        cout << "List is empty\n";
        return;
    }

    Node* temp1 = head;
    // Delete the head node
    if (position == 1)
    {
        head = head->next;
        delete temp1;
        return;
    }

    // Traverse to the (position - 1)th node
    for (int i = 0; i < position - 2; i++)
    {
        if (temp1 == nullptr || temp1->next == nullptr) 
        {
            cout << "Invalid position\n";
            return;
        }
        temp1 = temp1->next;
    }

    Node* temp2 = temp1->next;
    if (temp2 == nullptr) 
    {
        cout << "Invalid position\n";
        return;
    }

    temp1->next = temp2->next;
    delete temp2;
}

// Reversing the list using Iteration
Node* Reverse(Node* head)
{
    Node *current, *prev, *next;
    current = head;
    prev = nullptr;

    while (current != nullptr)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    head = prev;
    return head;
}

// Reversing the list using Recursion
void reverse_using_recursion(Node* _head)
{
    if (_head == nullptr)
    {
        head = _head;
        return;
    }
    Reverse(_head->next);
    Node* q = _head->next;
    q->next = _head;
    _head->next = nullptr;
}

// Printing the list in reverse order using Recursion
void reversePrint(Node* _head)
{
    if (_head == nullptr) { return; }
    reversePrint(_head->next);
    cout << _head->data << " -> ";
}

// Printing the list
void printList()
{
    Node* temp = head;
    while (temp != nullptr)
    {
        cout << temp->data << " -> ";
        temp = temp->next;
    }
    cout << "NULL\n";
}

// Printing the list using head node
void printList(Node* _head)
{
    Node* temp = _head;
    while (temp != nullptr)
    {
        cout << temp->data << " -> ";
        temp = temp->next;
    }
    cout << "NULL\n";
}

// Printing the list using Recursion
void print(Node* _head)
{
    if(_head == nullptr) return; 
    cout << _head->data << " -> ";
    print(_head->next);
}

// Main Function
int main() 
{
    insert(10, 1);
    insert(20, 2);
    insert(30, 3);
    insert(40, 4);
    insert(50, 5);

    cout << "Final list: \n";
    printList(head);

    head = Reverse(head);
    printList(head);
    reversePrint(head);
    cout << "\n";
    print(head);

    return 0;
}