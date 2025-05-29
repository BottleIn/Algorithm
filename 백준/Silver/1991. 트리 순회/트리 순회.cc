#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;
int N;

struct node {
	char left;
	char right;
};
vector <node> v(200);

void preOrder(char node) { 
	if (node == '.') return;

	cout << node;
	preOrder(v[node].left);
	preOrder(v[node].right);
}

void inorder(char node) {
	if (node == '.') return;
	
	inorder(v[node].left);
	cout << node ;
	inorder(v[node].right);
}
void postOrder(char node) {
	if (node == '.') return;

	postOrder(v[node].left);
	postOrder(v[node].right);
	cout << node;
}


int main() {
	cin >> N;
	char rt, l, r;
	for (int i = 0; i < N; i++) {
		cin >> rt >> l >> r;
		v[rt].left = l;
		v[rt].right = r;
	}
	preOrder('A');
	printf("\n");

	inorder('A');
	printf("\n");

	postOrder('A');
	printf("\n");
	return 0;
}
