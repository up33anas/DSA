#include <iostream>
using namespace std;

// Define the structure of a node in the linked list
struct Node {
    int data;       // The value stored in the node
    Node* next;     // Pointer to the next node
};

// Head pointer to point to the start of the list
Node* head = nullptr;

// Function to insert a node at a specific position
void insert(int data, int position) {
    // Create a new node and assign the data
    Node* temp1 = new Node();
    temp1->data = data;
    temp1->next = nullptr;

    // If inserting at the head (position 1)
    if (position == 1) {
        temp1->next = head;
        head = temp1;
        return;
    }

    // Traverse to the (position-1)th node
    Node* temp2 = head;
    for (int i = 0; i < position - 2; i++) {
        if (temp2 == nullptr) {
            cout << "Invalid position\n";
            return;
        }
        temp2 = temp2->next;
    }

    // Insert the new node at the desired position
    temp1->next = temp2->next;
    temp2->next = temp1;
    }
// Function to print the current list
void printList() {
    Node* temp = head;
    while (temp != nullptr) {
        cout << temp->data << " -> ";
        temp = temp->next;
    }
    cout << "NULL\n";
}

// Main function to test the insert function
int main() {
    // Insert elements into the list
    insert(10, 1); // List: 10
    insert(20, 2); // List: 10 -> 20
    insert(30, 1); // List: 30 -> 10 -> 20
    insert(40, 3); // List: 30 -> 10 -> 40 -> 20
    insert(50, 5); // List: 30 -> 10 -> 40 -> 20 -> 50

    // Print the final list
    cout << "Final Linked List: ";
    printList();

    return 0;
}
