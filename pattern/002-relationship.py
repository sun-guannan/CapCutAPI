import json
import random
import requests

# Set API keys
QWEN_API_KEY = "your qwen api key"
PEXELS_API_KEY = "your pexels api key"
CAPCUT_API_KEY = "your capcut api key"
LICENSE_KEY="your capcut license key", 


def llm(query = ""):
    """
    Call the Tongyi Qianwen large language model
    
    Parameters:
        
    Returns:
        dict: Dictionary containing title and list of sentences
    """
    
    # Build system prompt
    system_prompt = """
  * **Context:** You are an AI expert specializing in modern interpersonal relationships and emotional communication. Your knowledge base is built on a deep understanding of popular emotional content on social media, and you excel at interpreting the dynamics and perspectives of relationships in a relaxed, colloquial style.

  * **Objective:** When the user inputs "Give me some random returns", your goal is to **randomly create** advice about male-female emotions, behavioral habits, or relationship guidance. Your content must strictly mimic the unique style shown in the examples below.

  * **Style:** Your generated content should have the following characteristics:

      * **Structure:** Use a list format, with each point being a short, independent sentence.
      * **Wording:** Use colloquial language, often using the "When..." sentence pattern to describe a scenario.
      * **Theme:** Content should revolve around "how to understand the other person", "which behaviors are attractive", or "advice for a specific gender".

  * **Tone:** Your tone should be friendly, sincere, slightly teasing, like a friend sharing experiences on social media.

  * **Audience:** Your audience is anyone interested in modern emotional relationships who wants to get advice in a relaxed way.

  * **Response:** When you receive the instruction "Give me some random returns", please **randomly select one** from the following examples as your response. Or, you can **randomly generate** a new one with a completely consistent style, and return it in the same JSON format:

    **Example 1 (How to understand girls):**

    ```json
    {
      "title": "How to understand girls",
      "sentences": [
        "Hands on her stomach (Insecure)",
        "She leans on you (Feels safe)",
        "Covers her smile (Thinks your going to judge)",
        "Stops texting you (Feels like she is annoying you)",
        "Says she is fine (She is everything but fine)",
        "When she hugs you (You mean a lot to her)"
      ]
    }
    ```

    **Example 2 (Tips for girls):**

    ```json
    {
      "title": "Tips for the girls (From the guys)",
      "sentences": [
        "99/100 guys dont know what hip dips are and actually love your stretch marks",
        "We can't tell that you like us by just viewing our story, just message us",
        "When he's out with his boys, let him have this time (this is very important)",
        "'I'm not ready for a relationship' - unless your the luckiest girl in the world your not getting cuffed",
        "As Bruno mars said, 'your perfect just the way you are' so just be you, it'll work"
      ]
    }
    ```

    **Example 3 (Things guys find attractive in girls):**

    ```json
    {
      "title": "Things girls do that guys find attractive",
      "sentences": [
        "Bed hair when it's all messy >>>",
        "When you come work out with us",
        "Your sleepy voice in the morning or after a nap",
        "When you wear our t-shirts as pyjamas",
        "When you have a funny or really bad laugh",
        "When you initiate ...",
        "When your good with animals or animals like you"
      ]
    }
    ```
    """
    
    # Build user prompt
    user_prompt = f"Randomly create advice about male-female emotions, behavioral habits, or relationship guidance, based on user input: {query}"
    
    # Prepare request data
    url = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {QWEN_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "qwen-plus",
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        "temperature": 0.7,
        "max_tokens": 16384,
        "response_format": {"type": "json_object"}
    }
    
    try:
        # Send HTTP request
        response = requests.post(url, headers=headers, json=data, timeout=30)
        
        # Check response status
        if response.status_code == 200:
            response_data = response.json()
            
            # Extract content from response
            if 'choices' in response_data and len(response_data['choices']) > 0:
                content = response_data['choices'][0]['message']['content']
                
                try:
                    # Parse JSON response
                    result = json.loads(content)
                    
                    # Ensure result contains necessary fields
                    if "title" in result and "sentences" in result:
                        return result
                except json.JSONDecodeError:
                    pass  # If JSON parsing fails, will return predefined example
        
        # If API call fails or parsing fails, print error message
        print(f"Error: {response.status_code}, {response.text if hasattr(response, 'text') else 'No response text'}")
    except Exception as e:
        # Catch all possible exceptions
        print(f"Exception occurred: {str(e)}")


def search_pexels_videos(query="twilight", min_duration=10, orientation="portrait", per_page=15):
    """
    Call Pexels API to search for videos
    
    Parameters:
        query (str): Search keyword, default is "twilight"
        min_duration (int): Minimum video duration (seconds), default is 10 seconds
        orientation (str): Video orientation, default is "portrait"
        per_page (int): Number of results per page, default is 15
        
    Returns:
        list: List containing video information
    """
    url = "https://api.pexels.com/videos/search"
    headers = {
        "Authorization": PEXELS_API_KEY
    }
    params = {
        "query": query,
        "orientation": orientation,
        "per_page": per_page,
        "min_duration": min_duration
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            data = response.json()
            videos = []
            
            for video in data.get("videos", []):
                # Get video file information
                video_files = video.get("video_files", [])
                # Filter out 16:9 ratio video files
                portrait_videos = [file for file in video_files 
                                 if file.get("width") and file.get("height") and 
                                 file.get("height") / file.get("width") > 1.7]  # Close to 16:9 ratio
                
                if portrait_videos:
                    # Select highest quality video file
                    best_quality = max(portrait_videos, key=lambda x: x.get("width", 0) * x.get("height", 0))
                    
                    videos.append({
                        "id": video.get("id"),
                        "url": video.get("url"),
                        "image": video.get("image"),
                        "duration": video.get("duration"),
                        "user": video.get("user", {}).get("name"),
                        "video_url": best_quality.get("link"),
                        "width": best_quality.get("width"),
                        "height": best_quality.get("height"),
                        "file_type": best_quality.get("file_type")
                    })
            
            if videos:
                random_video = random.choice(videos)
                return random_video['video_url']
            return []
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return []
    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return []


def create_capcut_draft(width=1080, height=1920):
    """
    Call CapCut API to create a new draft
    
    Parameters:
        width (int): Video width, default is 1080
        height (int): Video height, default is 1920
        
    Returns:
        dict: Dictionary containing draft ID and download URL, or error message if failed
    """
    url = "https://open.capcutapi.top/cut_jianying/create_draft"
    headers = {
        "Authorization": f"Bearer {CAPCUT_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "width": width,
        "height": height
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            result = response.json()
            
            if result.get("success"):
                return {
                    "success": True,
                    "draft_id": result.get("output", {}).get("draft_id"),
                    "draft_url": result.get("output", {}).get("draft_url")
                }
            else:
                return {
                    "success": False,
                    "error": result.get("error", "Unknown error")
                }
        else:
            return {
                "success": False,
                "error": f"HTTP Error: {response.status_code}",
                "response": response.text
            }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


def add_video_to_draft(draft_id, video_url):
    """
    Call CapCut API to add video to draft
    
    Parameters:
        draft_id (str): Draft ID
        video_url (str): Video URL
        
    Returns:
        dict: Dictionary containing draft ID and download URL, or error message if failed
    """
    url = "https://open.capcutapi.top/cut_jianying/add_video"
    headers = {
        "Authorization": f"Bearer {CAPCUT_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "video_url": video_url,
        "draft_id": draft_id,
        "end": 10  # Set video duration to 10 seconds
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            result = response.json()
            
            if result.get("success"):
                return {
                    "success": True,
                    "draft_id": result.get("output", {}).get("draft_id"),
                    "draft_url": result.get("output", {}).get("draft_url")
                }
            else:
                return {
                    "success": False,
                    "error": result.get("error", "Unknown error")
                }
        else:
            return {
                "success": False,
                "error": f"HTTP Error: {response.status_code}",
                "response": response.text
            }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

def add_text_to_draft(draft_id, text, font="ZY_Starry", 
font_color="#FFFFFF", 
background_color="#000000", 
background_alpha=0.5,
background_style=2,
background_round_radius=10,
 transform_y=0, 
 transform_x=0, 
 font_size=10.0,
 fixed_width=0.6,
 track_name="text_main"):
    """
    Call CapCut API to add text to draft
    
    Parameters:
        draft_id (str): Draft ID
        text (str): Text content
        start_time (float): Text start time on timeline (seconds), default is 0
        end_time (float): Text end time on timeline (seconds), default is 5
        font (str): Font, default is "ZY_Starry"
        font_color (str): Font color, default is white
        background_color (str): Background color, default is black
        background_alpha (float): Background transparency, default is 0.5
        transform_y (float): Y-axis position offset, default is 0
        transform_x (float): X-axis position offset, default is 0
        font_size (float): Font size, default is 10.0
        
    Returns:
        dict: Dictionary containing draft ID and download URL, or error message if failed
    """
    url = "https://open.capcutapi.top/cut_jianying/add_text"
    headers = {
        "Authorization": f"Bearer {CAPCUT_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "start": 0,
        "end": 10,
        "draft_id": draft_id,
        "font": font,
        "font_color": font_color,
        "font_size": font_size,
        "transform_y": transform_y,
        "transform_x": transform_x,
        "fixed_width": fixed_width,
        "background_color": background_color,
        "background_alpha": background_alpha,
        "background_style": background_style,
        "background_round_radius": background_round_radius,
        "track_name": track_name
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            result = response.json()
            
            if result.get("success"):
                return {
                    "success": True,
                    "draft_id": result.get("output", {}).get("draft_id"),
                    "draft_url": result.get("output", {}).get("draft_url")
                }
            else:
                return {
                    "success": False,
                    "error": result.get("error", "Unknown error")
                }
        else:
            return {
                "success": False,
                "error": f"HTTP Error: {response.status_code}",
                "response": response.text
            }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

def generate_video(draft_id, resolution="720P", framerate="24"):
    """
    Call CapCut API to render video
    
    Parameters:
        draft_id (str): Draft ID
        license_key (str): License key
        resolution (str): Video resolution, default is "720P"
        framerate (str): Video frame rate, default is "24"
        
    Returns:
        dict: Dictionary containing task ID, or error message if failed
    """
    url = "https://open.capcutapi.top/cut_jianying/generate_video"
    headers = {
        "Authorization": f"Bearer {CAPCUT_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "draft_id": draft_id,
        "license_key": LICENSE_KEY,
        "resolution": resolution,
        "framerate": framerate
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            result = response.json()
            
            if result.get("success"):
                return {
                    "success": True,
                    "task_id": result.get("output", {}).get("task_id")
                }
            else:
                return {
                    "success": False,
                    "error": result.get("error", "Unknown error")
                }
        else:
            return {
                "success": False,
                "error": f"HTTP Error: {response.status_code}",
                "response": response.text
            }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

def check_task_status(task_id):
    """
    Call CapCut API to check task status
    
    Parameters:
        task_id (str): Task ID
        
    Returns:
        dict: Dictionary containing task status and results, or error message if failed
    """
    url = "https://open.capcutapi.top/cut_jianying/task_status"
    headers = {
        "Authorization": f"Bearer {CAPCUT_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "task_id": task_id
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            result = response.json()
            
            if result.get("success"):
                output = result.get("output", {})
                return {
                    "success": True,
                    "status": output.get("status"),
                    "progress": output.get("progress"),
                    "result": output.get("result"),  # Video URL
                    "error": output.get("error")
                }
            else:
                return {
                    "success": False,
                    "error": result.get("error", "Unknown error")
                }
        else:
            return {
                "success": False,
                "error": f"HTTP Error: {response.status_code}",
                "response": response.text
            }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


# Example usage
if __name__ == "__main__":

    # Call LLM function and print result
    result = llm()
    print(json.dumps(result, indent=2, ensure_ascii=False))

    # 1. Create draft
    draft_result = create_capcut_draft()
    print("Draft creation result:", json.dumps(draft_result, indent=2, ensure_ascii=False))
    
    if draft_result.get("success"):

        draft_id = draft_result.get("draft_id")

        # 2. Search Pexels videos
        video_url = search_pexels_videos()
        print("Pexels video URL:", video_url)
        
        # 3. Add video to draft
        if video_url:
            add_result = add_video_to_draft(draft_result.get("draft_id"), video_url)
            print("Add video result:", json.dumps(add_result, indent=2, ensure_ascii=False))
    

        # 5. Add title text
        title_result = add_text_to_draft(
            draft_id=draft_id,
            text=result["title"],
            font="ZY_Starry",  # Use starry font
            font_color="#FFFFFF",  # White font
            background_color="#000000",  # Black background
            background_alpha=1,  # Background transparency
            background_style=1,
            background_round_radius=10,
            transform_y=0.7,  # Located at the top of the screen (1 is top edge, -1 is bottom edge)
            transform_x=0,  # Horizontally centered
            font_size=13.0,  # Larger font
            track_name = "title",
            fixed_width=0.6
        )
        print("Add title result:", json.dumps(title_result, indent=2, ensure_ascii=False))
        
        # 6. Add sentence text
        sentence_count = len(result["sentences"])
        for i, sentence in enumerate(result["sentences"]):
            # Calculate vertical position - evenly distributed in the middle of the screen
            transform_y = 0.5 - (1.1 * (i + 1) / (sentence_count + 1))
            
            # Determine horizontal alignment - odd sentences left-aligned, even sentences right-aligned
            if i % 2 == 0:  # Odd sentences (counting from 0)
                transform_x = -0.5  # Left-aligned
            else:  # Even sentences
                transform_x = 0.5  # Right-aligned
            
            sentence_result = add_text_to_draft(
                draft_id=draft_id,
                text=sentence,
                font="ZY_Fantasy",  # Use fantasy font
                font_color="#FFFFFF",  # White font
                transform_y=transform_y,  # Vertical position
                transform_x=transform_x,  # Horizontal position (left-right alignment)
                background_alpha=0,
                font_size=7.0,  # Smaller font
                fixed_width=0.3,
                track_name=f"text_{i}"
            )
            print(f"Add sentence {i+1} result:", json.dumps(sentence_result, indent=2, ensure_ascii=False))

        # 7. Render video
        print("\nStarting video rendering...")
        generate_result = generate_video(draft_id)
        print("Video rendering request result:", json.dumps(generate_result, indent=2, ensure_ascii=False))
        
        if generate_result.get("success"):
            task_id = generate_result.get("task_id")
            print(f"Task ID: {task_id}, starting to poll task status...")
            
            # 8. Poll task status
            import time
            max_attempts = 30  # Maximum 30 polling attempts
            attempt = 0
            
            while attempt < max_attempts:
                status_result = check_task_status(task_id)
                print(f"Poll count {attempt+1}, status:", json.dumps(status_result, indent=2, ensure_ascii=False))
                
                if not status_result.get("success"):
                    print("Failed to check task status:", status_result.get("error"))
                    break
                
                status = status_result.get("status")
                if status == "SUCCESS":
                    print("\nVideo rendering successful!")
                    print("Video URL:", status_result.get("result"))
                    break
                elif status == "FAILED":
                    print("\nVideo rendering failed:", status_result.get("error"))
                    break
                
                # Wait 5 seconds before checking again
                print("Waiting 5 seconds before checking again...")
                time.sleep(5)
                attempt += 1
            
            if attempt >= max_attempts:
                print("\nPolling timeout, please check task status manually later")