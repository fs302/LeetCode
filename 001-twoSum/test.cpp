#include <iostream>
#include <vector>
#include "twoSum.cpp"
using namespace std;

void foo()
{
    Solution t;
    vector<int> numbers;
    numbers.push_back(3);
    numbers.push_back(2);
    numbers.push_back(4);
    int target = 6;
    vector<int> result = t.twoSum(numbers, target);
    if (result.size()>=2)
    {
        cout << result[0] << " " <<result[1] << endl;
    }
}

int main()
{
    foo();
    return 0;
}


