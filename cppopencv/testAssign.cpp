#include <opencv/cv.h>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <iostream>
#include <vector>

using namespace cv;
using namespace std;
cv::Mat src = cv::imread("../dataSet/playground/back.png", cv::IMREAD_GRAYSCALE);

static Mat drawing = Mat::zeros( src.size(), CV_8UC3 );
int main()
{
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
	// bitwise_and(src,mask,src);
	std::vector<vector<Point> > contours;
	std::vector<Vec4i> hierarchy;
  	cv::findContours(src, contours, hierarchy, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, Point(0, 0) );

	for( int i = 0; i< contours.size(); i++ )
		{
			Scalar color = Scalar( 0,255,255 );
			drawContours( drawing, contours, i, color, 2, 8, hierarchy, 0, Point(0,0) );
		}
	cv::imshow("origin", src);
	cv::imshow("mask", mask);
	cv::imshow("contours", drawing);
	cv::waitKey(0);

}
