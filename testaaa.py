from django.http import JsonResponse
import subprocess

def your_a_view(request):
    try:
        # Execute B.py and capture its output
        result = subprocess.run(['python', 'path/to/B.py'], capture_output=True, text=True)
        
        if result.returncode == 0:
            # Get the output from B.py
            output_from_B = result.stdout.strip()

            # Continue with the rest of your A.py logic using output_from_B
            # ...

            return JsonResponse({'output_from_B': output_from_B})
        else:
            return JsonResponse({'error': 'Error executing B.py'}, status=500)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

