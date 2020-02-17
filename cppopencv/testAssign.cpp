#include <opencv/cv.h>
#include <iostream>
static cv::Mat sta;
const int s = 2;
int a[s]={2,4};
void func()
{
	cv::Mat f = (cv::Mat_<double>(2,2) << 5.0, 5.0, 5.0, 5.0);	
	sta = f;

}
int main()
{
		cv::Mat A = (cv::Mat_<double>(2,2) << 1.0, 2.0, 3.0, 4.0);
		cv::Mat C = (cv::Mat_<double>(2,2) << 5555,2.0, 3.0, 4.0);
		std::cout << "Original A:\n" << A << std::endl;
		
		cv::Mat B = A;
		B.at<double>(0, 1) = 2.5;
		std::cout << "A:\n" << A << std::endl;

		A = C;
		C.at<double>(1, 1) = 28282;
		std::cout << "A:\n" << A << std::endl;

		func();
		std::cout << "sta:\n" << sta << std::endl;
		int x = 1;
		int a[2]={2,4};
		a[x%1] = 0;
		std::cout << a[0] << std::endl;

}
