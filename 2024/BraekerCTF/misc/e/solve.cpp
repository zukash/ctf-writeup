// #include <sys/auxv.h>

#include <iostream>
#include <random>
#include <sys/auxv.h>
using namespace std;


void add_user_input(vector<float> *n_arr, string msg) {
	float input;
	cout << msg << endl;
	cin >> input;
	n_arr->push_back(input);
}

int main(void) {
	vector<float> n_arr;

  // Random seed
	unsigned int *seed;
  seed = (unsigned int *)getauxval(AT_RANDOM);
  srand(*seed);
  // cout << *seed << endl;
	for (int i = 0; i < 1024 * (8 + rand() % 1024); i++)
		n_arr.push_back((rand() % 1024) + 1);

  n_arr.push_back(numeric_limits<float>::max());
  n_arr.push_back(-numeric_limits<float>::max());


	float total = 0;
	for (int i = 0; i < n_arr.size(); i++)
		total += n_arr[i];

  cout << total << endl;
  cout << numeric_limits<float>::min() << endl;
  cout << numeric_limits<float>::max() << endl;
  cout << -numeric_limits<float>::max() << endl;

}