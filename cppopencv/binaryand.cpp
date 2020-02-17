#include <opencv/cv.h>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>
int main()
{
	cv::Mat src = cv::imread("../dataSet/playground/back.png", cv::IMREAD_GRAYSCALE);
	cv::Mat mask = cv::Mat::zeros(src.size(), src.type());
	std::cout << src.rows/2 << std::endl;
	std::cout << src.cols << std::endl;
	std::cout << mask.rows/2 << std::endl;
	std::cout << mask.cols << std::endl;

	//mask=(mask&cv::Scalar(255));
	mask(cv::Range(0,mask.rows),cv::Range(0,mask.cols/2))=255;
	cv::Mat res;
	//res = src&mask;
	// bitwise_and(src,src,res,mask);
	bitwise_and(src,mask,src);
	cv::imshow("origin", src);
	cv::imshow("mask", mask);
	cv::imshow("res", src);
	cv::waitKey(0);

}
