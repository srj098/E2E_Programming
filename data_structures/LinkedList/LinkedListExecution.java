package com.srj.linkedList;

public class LinkedListExecution {
	
public static void main(String[] args) {
	
	LinkedList list = new LinkedList();
	list.addElement(5);
	list.addElement(10);
	list.addElement(15);
	list.addElementStart(18);
	list.addElementAt(2, 17);
	list.printAll();
	
}
}