package com.srj.linkedList;


public class LinkedList implements LinkedListInterface {
	Node head;

//Implementation of adding the elements into the list
	
	public void addElement(int data) {
		Node node = new Node();
		node.element =data;
		node.next = null;
		if(head==null) {
			head = node;
		}else {
			Node n=head;
			while(n.next!=null) {
				n=n.next;
			}
			n.next=node;
		}
	}
	
	public void addElementStart(int data) {
		Node node =new Node();
		node.element =data;
		node.next = null;
		node.next = head;
		head =node;	
	}
	
	public void addElementAt(int index, int data) {
		Node node =new Node();
		node.element =data;
		node.next =null;
		Node n =head;
		for(int i=0;i<index-1;i++) {
			n=n.next;
		}
		node.next=n.next;
		n.next=node;
	}
	
//Implementation of removing the elements from the list
	
	public void deleteAt(int index) {
		
	}
	
//Implementation of printing all the elements of the list
	
	public void printAll() {
		Node n =head;
		while(n.next!=null) {
			System.out.println(n.element);
			n=n.next;
		}
		System.out.println(n.element);
		
	}
		
	}
	

