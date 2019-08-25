package main

import (
	"container/heap"
)

type maxHeap []int
type minHeap []int

func (h maxHeap) Max() int           { return h[0] }
func (h maxHeap) Len() int           { return len(h) }
func (h maxHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h maxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *maxHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *maxHeap) Pop() interface{} {
	max := (*h)[0]
	*h = (*h)[:h.Len()]
	return max
}

func (h minHeap) Min() int           { return h[0] }
func (h minHeap) Len() int           { return len(h) }
func (h minHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h minHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *minHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *minHeap) Pop() interface{} {
	min := (*h)[0]
	*h = (*h)[:h.Len()]
	return min
}

type MedianFinder struct {
	maxH *maxHeap // left max-heap
	minH *minHeap // right min-heap
	size int
}

func Constructor() MedianFinder {
	maxH := &maxHeap{}
	minH := &minHeap{}
	return MedianFinder{maxH, minH, 0}
}

func (this *MedianFinder) AddNum(num int) {
	if this.size%2 == 0 {
		heap.Push(this.maxH, num)
	} else {
		heap.Push(this.minH, num)
	}
	this.size++
	if this.size > 2 && (this.maxH.Max() > this.minH.Min()) {
		(*this.maxH)[0], (*this.minH)[0] = (*this.minH)[0], (*this.maxH)[0]
		heap.Fix(this.maxH, 0)
		heap.Fix(this.minH, 0)
	}
}

func (this *MedianFinder) FindMedian() float64 {
	if this.size%2 == 0 {
		return float64(this.maxH.Max()+this.minH.Min()) / 2
	}
	return float64(this.maxH.Max())
}
