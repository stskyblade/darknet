#include <time.h>

void wait_for (unsigned int secs) {
  unsigned int retTime = time(0) + secs;   // Get finishing time.
  while (time(0) < retTime);               // Loop until it arrives.
}

void sleep_msg (char *msg, unsigned int secs) {
  printf("%s sleep %d\n", msg, secs);
  wait_for(secs);
}
