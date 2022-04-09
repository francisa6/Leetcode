#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;
// using std::vector;
// using std::unordered_map;

class Solution {
public:
  vector<int> twoSum(vector<int> &nums, int target) {
    unordered_map<int, int> indices;
    for (int i = 0; i < nums.size(); i++) {
      if (indices.find(target - nums[i]) != indices.end()) {
        return {indices[target - nums[i]], i};
      }
      indices[nums[i]] = i;
    }
    return {};
  }
};

int main() {
  Solution sol;
  // vector<int> nums = {3,3};
  // int target = 6;
  cout << "sol: " << sol.twoSum({3, 3}, 6);
  return 0;
}
