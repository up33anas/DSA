#include <iostream>

using namespace std;

struct Node
{
    int data;
    Node* next;
    Node* prev;
};

Node* head;

Node* get_new_node(int x)
{
    Node* temp = new Node();
    temp->data = x;
    temp->next = nullptr;
    temp->prev = nullptr;
    return temp;
}

void insert_at_head(int x)
{
    Node* newNode = get_new_node(x);
    if (head == nullptr)
    {
        head = newNode;
        return;
    }
    head->prev = newNode;
    newNode->next = head;
    head = newNode;
}

void print()
{
    Node* temp = head;
    cout << "Forward: ";
    while (temp != nullptr)
    {
        cout << temp->data << " -> ";
        temp = temp->next;
    }
    cout << endl;
}

void reverse_print()
{
    Node* temp = head;
    if (temp == nullptr)
    {
        return;
    }

    while (temp->next != nullptr)
    {
        temp = temp->next;
    }
    
    cout << "Reverse: ";
    while (temp != nullptr)
    {
        cout << temp->data << " -> ";
        temp = temp->prev;
    }
    cout << endl;
}

int main() 
{
    head = nullptr;
    insert_at_head(2); print(); reverse_print();
    insert_at_head(3); print(); reverse_print();
    insert_at_head(4); print(); reverse_print();
    insert_at_head(5); print(); reverse_print();
    insert_at_head(6); print(); reverse_print();

    return 0;
}