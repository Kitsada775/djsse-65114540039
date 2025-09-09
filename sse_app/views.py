from django.http import StreamingHttpResponse
from django.shortcuts import render
import time

def event_stream():
    """Generator สำหรับ SSE"""
    try:
        print("SSE stream started")
        
        for i in range(101):
            data = f"data: {i}\n\n"
            print(f"Sending: {i}%")
            yield data
            
            if i < 100:
                time.sleep(3)  # ส่งทุก 5 วินาที
                
        print("SSE stream completed")
        
    except Exception as e:
        print(f"Error in event_stream: {e}")
        yield f"data: Error: {str(e)}\n\n"

def event_stream_view(request):
    """SSE endpoint"""
    try:
        print("SSE request received")
        
        response = StreamingHttpResponse(
            event_stream(),
            content_type='text/event-stream'
        )
        
        response['Cache-Control'] = 'no-cache'
        # response['Connection'] = 'keep-alive'  # <-- ลบบรรทัดนี้ออก
        response['Access-Control-Allow-Origin'] = '*'
        
        return response
        
    except Exception as e:
        print(f"Error in event_stream_view: {e}")
        from django.http import HttpResponse
        return HttpResponse(f"Error: {str(e)}", status=500)

def index(request):
    return render(request, 'sse_app/index.html')