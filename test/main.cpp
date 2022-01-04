#include <iostream>
#include "cmake-build-debug/test.pb.h"

int main() {
  TestObj t;
  t.add_z(123);
  t.add_z(456);
  auto* b1 = t.mutable_t()->add_bases();
  b1->set_a(1);
  auto* b2 = t.mutable_t()->add_bases();
  b2->set_a(2);
  std::vector<int> y;
  y.push_back(123);
  auto py = &y;
  auto& ry = y;
  auto pz = t.mutable_z();
  auto pt = t.mutable_t()->mutable_bases();
  auto& rz = *t.mutable_z();
  auto& rt = *t.mutable_t()->mutable_bases();
  return 0;
}
