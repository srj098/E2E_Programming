package com.srj.linkedList;

public interface LinkedListInterface {

//insert elements into the list
void addElement(int data);

void addElementAt(int index, int data);

void addElementStart(int data);

//Remove elements from the list
void deleteAt(int index);

//print all the elements
void printAll();

}
