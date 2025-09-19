import pyJianYingDraft as draft
from pyJianYingDraft import exceptions
from create_draft import get_or_create_draft
from typing import Optional, Dict, List
from draft_cache import update_cache

from util import generate_draft_url

def add_video_keyframe_impl(
    draft_id: Optional[str] = None,
    track_name: str = "main",
    property_type: str = "alpha",
    time: float = 0.0,
    value: str = "1.0",
    property_types: Optional[List[str]] = None,
    times: Optional[List[float]] = None,
    values: Optional[List[str]] = None
) -> Dict[str, str]:
    """
    Add keyframes to the specified segment
    :param draft_id: Draft ID, if None or corresponding zip file not found, a new draft will be created
    :param track_name: Track name, default "main"
    :param property_type: Keyframe property type, supports the following values:
        - position_x: Horizontal position, range [-1,1], 0 means center, 1 means rightmost
        - position_y: Vertical position, range [-1,1], 0 means center, 1 means bottom
        - rotation: Clockwise rotation angle
        - scale_x: X-axis scale ratio (1.0 means no scaling), mutually exclusive with uniform_scale
        - scale_y: Y-axis scale ratio (1.0 means no scaling), mutually exclusive with uniform_scale
        - uniform_scale: Overall scale ratio (1.0 means no scaling), mutually exclusive with scale_x and scale_y
        - alpha: Opacity, 1.0 means completely opaque
        - saturation: Saturation, 0.0 means original saturation, range from -1.0 to 1.0
        - contrast: Contrast, 0.0 means original contrast, range from -1.0 to 1.0
        - brightness: Brightness, 0.0 means original brightness, range from -1.0 to 1.0
        - volume: Volume, 1.0 means original volume
    :param time: Keyframe time point (seconds), default 0.0
    :param value: Keyframe value, format varies according to property_type:
        - position_x/position_y: "0" means center position, range [-1,1]
        - rotation: "45deg" means 45 degrees
        - scale_x/scale_y/uniform_scale: "1.5" means scale up by 1.5 times
        - alpha: "50%" means 50% opacity
        - saturation/contrast/brightness: "+0.5" means increase by 0.5, "-0.5" means decrease by 0.5
        - volume: "80%" means 80% of original volume
    :param property_types: Batch mode: List of keyframe property types, e.g. ["alpha", "position_x", "rotation"]
    :param times: Batch mode: List of keyframe time points (seconds), e.g. [0.0, 1.0, 2.0]
    :param values: Batch mode: List of keyframe values, e.g. ["1.0", "0.5", "45deg"]
    Note: property_types, times, values must be provided together and have equal lengths. If these parameters are provided, single keyframe parameters will be ignored
    :return: Updated draft information
    """
    # Get or create draft
    draft_id, script = get_or_create_draft(
        draft_id=draft_id
    )
    
    try:
        # Get specified track
        track = script.get_track(draft.Video_segment, track_name=track_name)
        
        # Get segments in the track
        segments = track.segments
        if not segments:
            raise Exception(f"No segments in track {track_name}")
        
        # Determine the keyframes list to process
        if property_types is not None or times is not None or values is not None:
            # Batch mode: use three array parameters
            if property_types is None or times is None or values is None:
                raise Exception("In batch mode, property_types, times, values must be provided together")
            
            if not (isinstance(property_types, list) and isinstance(times, list) and isinstance(values, list)):
                raise Exception("property_types, times, values must all be list types")
            
            if len(property_types) == 0:
                raise Exception("In batch mode, parameter lists cannot be empty")
            
            if not (len(property_types) == len(times) == len(values)):
                raise Exception(f"property_types, times, values must have equal lengths, current lengths are: {len(property_types)}, {len(times)}, {len(values)}")
            
            keyframes_to_process = [
                {
                    "property_type": prop_type,
                    "time": t,
                    "value": val
                }
                for prop_type, t, val in zip(property_types, times, values)
            ]
        else:
            # Single mode: use original parameters
            keyframes_to_process = [{
                "property_type": property_type,
                "time": time,
                "value": value
            }]
        
        # Process each keyframe
        added_count = 0
        for i, kf in enumerate(keyframes_to_process):
            try:
                _add_single_keyframe(track, kf["property_type"], kf["time"], kf["value"])
                added_count += 1
            except Exception as e:
                raise Exception(f"Failed to add keyframe #{i+1} (property_type={kf['property_type']}, time={kf['time']}, value={kf['value']}): {str(e)}")
        
        result = {
            "draft_id": draft_id,
            # "draft_url": generate_draft_url(draft_id)
        }
        
        # If in batch mode, return the number of added keyframes
        if property_types is not None:
            result["added_keyframes_count"] = added_count
        
        # Persist updated script
        update_cache(draft_id, script)

        return result
        
    except exceptions.TrackNotFound:
        raise Exception(f"Track named {track_name} not found")
    except Exception as e:
        raise Exception(f"Failed to add keyframe: {str(e)}")


def _add_single_keyframe(track, property_type: str, time: float, value: str):
    """
    Internal function to add a single keyframe
    """
    # Convert property type string to enum value, validate if property type is valid
    try:
        property_enum = getattr(draft.Keyframe_property, property_type)
    except:
        raise Exception(f"Unsupported keyframe property type: {property_type}")
        
    # Parse value based on property type
    try:
        if property_type in ['position_x', 'position_y']:
            # Handle position, range [0,1]
            float_value = float(value)
            if not -10 <= float_value <= 10:
                raise ValueError(f"Value for {property_type} must be between -10 and 10")
        elif property_type == 'rotation':
            # Handle rotation angle
            if value.endswith('deg'):
                float_value = float(value[:-3])
            else:
                float_value = float(value)
        elif property_type == 'alpha':
            # Handle opacity
            if value.endswith('%'):
                float_value = float(value[:-1]) / 100
            else:
                float_value = float(value)
        elif property_type == 'volume':
            # Handle volume
            if value.endswith('%'):
                float_value = float(value[:-1]) / 100
            else:
                float_value = float(value)
        elif property_type in ['saturation', 'contrast', 'brightness']:
            # Handle saturation, contrast, brightness
            if value.startswith('+'):
                float_value = float(value[1:])
            elif value.startswith('-'):
                float_value = -float(value[1:])
            else:
                float_value = float(value)
        else:
            # Other properties directly convert to float
            float_value = float(value)
    except ValueError:
        raise Exception(f"Invalid value format: {value}")
    
    # If track object is provided, use the track's add_pending_keyframe method
    track.add_pending_keyframe(property_type, time, value)