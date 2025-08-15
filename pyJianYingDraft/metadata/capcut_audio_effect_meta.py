from .effect_meta import EffectEnum
from .effect_meta import EffectMeta, EffectParam

class CapCutVoiceFiltersEffectType(EffectEnum):
    """CapCut自带的Voice filters特效类型"""

    Big_House    = EffectMeta("Big House", False, "7350559836590838274", "8954C5C2-A0BB-4915-8CB2-B422445DCB71", "3b1d62bbe927104e393b0fc5043dc0a6", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
        - strength: 默认1.00, 0.00 ~ 1.00
    """
    Low          = EffectMeta("Low", False, "7021052731091587586", "4D23A0EA-5E4B-4B6A-8CE7-E3B0ADAFBCE1", "e2e27786b25e4cf9b4e74558d6f6c832", [
                              EffectParam("change_voice_param_pitch", 0.375, 0.000, 1.000),
                              EffectParam("change_voice_param_timbre", 0.250, 0.000, 1.000)])
    """参数:
        - change_voice_param_pitch: 默认0.38, 0.00 ~ 1.00
        - change_voice_param_timbre: 默认0.25, 0.00 ~ 1.00
    """
    Energetic    = EffectMeta("Energetic", False, "7320193885114733057", "FA559CAA-D9AA-443B-9D39-392B43D2DB02", "99fee98d58dd023a9f54a772dffe1ac1", [
                              EffectParam("Intensity", 1.000, 0.000, 1.000)])
    """参数:
        - Intensity: 默认1.00, 0.00 ~ 1.00
    """
    High         = EffectMeta("High", False, "7021052551755731457", "E663A5D0-A024-4DED-8F0D-DA6D70A9F50C", "a83c56bd3fb17e93a1437d06498ab7ec", [
                              EffectParam("change_voice_param_pitch", 0.834, 0.000, 1.000),
                              EffectParam("change_voice_param_timbre", 0.334, 0.000, 1.000)])
    """参数:
        - change_voice_param_pitch: 默认0.83, 0.00 ~ 1.00
        - change_voice_param_timbre: 默认0.33, 0.00 ~ 1.00
    """
    Low_Battery  = EffectMeta("Low Battery", False, "7021052694370456065", "3FB0AA17-B7E8-4820-86A2-0A34E3F2F881", "a96ff559c9f1afec0603ae8bb107d98c", [
                              EffectParam("change_voice_param_strength", 1.000, 0.000, 1.000)])
    """参数:
        - change_voice_param_strength: 默认1.00, 0.00 ~ 1.00
    """
    Tremble      = EffectMeta("Tremble", False, "7021052770924892674", "4AEE9A06-71E0-4188-A87E-A161DDB80F4A", "337b1ba48ea61c95ac84ba238598ca0c", [
                              EffectParam("change_voice_param_frequency", 0.714, 0.000, 1.000),
                              EffectParam("change_voice_param_width", 0.905, 0.000, 1.000)])
    """参数:
        - change_voice_param_frequency: 默认0.71, 0.00 ~ 1.00
        - change_voice_param_width: 默认0.91, 0.00 ~ 1.00
    """
    Electronic   = EffectMeta("Electronic", False, "7021052717204247042", "0285BDC4-794F-48D0-A8BD-78B248FDE822", "a6f883d8294fd5f49952cbf08544a0c5", [
                              EffectParam("change_voice_param_strength", 1.000, 0.000, 1.000)])
    """参数:
        - change_voice_param_strength: 默认1.00, 0.00 ~ 1.00
    """
    Sweet        = EffectMeta("Sweet", False, "7320193577613529602", "2CD71FC4-7B4E-4E53-B337-32173184F480", "ac2110d039d35ad01ca8452a6eadc921", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
        - strength: 默认1.00, 0.00 ~ 1.00
    """
    Vinyl        = EffectMeta("Vinyl", False, "7025484451710767618", "6D42DEB5-D9DE-479F-955C-9F63C3B88F06", "fe8fdb1bcec05647749e076a15443f08", [
                              EffectParam("change_voice_param_strength", 1.000, 0.000, 1.000),
                              EffectParam("change_voice_param_noise", 0.743, 0.000, 1.000)])
    """参数:
        - change_voice_param_strength: 默认1.00, 0.00 ~ 1.00
        - change_voice_param_noise: 默认0.74, 0.00 ~ 1.00
    """
    Mic_Hog      = EffectMeta("Mic Hog", False, "7021052785101640194", "9A48AB2D-B527-4DF0-8512-058819047877", "f2bab335416833134ab4bb780c128cd2", [
                              EffectParam("change_voice_param_room", 0.052, 0.000, 1.000),
                              EffectParam("change_voice_param_strength", 0.450, 0.000, 1.000)])
    """参数:
        - change_voice_param_room: 默认0.05, 0.00 ~ 1.00
        - change_voice_param_strength: 默认0.45, 0.00 ~ 1.00
    """
    LoFi         = EffectMeta("Lo-Fi", False, "7025484400313766402", "1C8426BF-AC3B-4F90-B145-CA712BD486D3", "44a00f0e2b85e0006f49ef345a305ec1", [
                              EffectParam("change_voice_param_strength", 1.000, 0.000, 1.000)])
    """参数:
        - change_voice_param_strength: 默认1.00, 0.00 ~ 1.00
    """
    Megaphone    = EffectMeta("Megaphone", False, "7021052620592648705", "8A5CF5B8-0959-4E8A-8CC5-AD17BA176D89", "b2ca5803b90f44ee0c833f34ef684d40", [
                              EffectParam("change_voice_param_strength", 1.000, 0.000, 1.000)])
    """参数:
        - change_voice_param_strength: 默认1.00, 0.00 ~ 1.00
    """
    Echo         = EffectMeta("Echo", False, "7021052523762946561", "83B7B5D7-B539-4FAA-8CF3-3318394C9278", "c37d02ae5853211ad84c13e6dca31b81", [
                              EffectParam("change_voice_param_quantity", 0.800, 0.000, 1.000),
                              EffectParam("change_voice_param_strength", 0.762, 0.000, 1.000)])
    """参数:
        - change_voice_param_quantity: 默认0.80, 0.00 ~ 1.00
        - change_voice_param_strength: 默认0.76, 0.00 ~ 1.00
    """
    Synth        = EffectMeta("Synth", False, "7021052503919694337", "450DE367-AD03-4D06-B635-C947161AAA8E", "0247a95158fda7a9e44ccd4f832a9a14", [
                              EffectParam("change_voice_param_strength", 1.000, 0.000, 1.000)])
    """参数:
        - change_voice_param_strength: 默认1.00, 0.00 ~ 1.00
    """
    Deep         = EffectMeta("Deep", False, "7021052537344102913", "188C5140-E4AC-41A5-B42A-901ACAEF1B62", "583e3ccf9d2daad3860aa70ad61b64ca", [
                              EffectParam("change_voice_param_pitch", 0.834, 0.000, 1.000),
                              EffectParam("change_voice_param_timbre", 1.000, 0.000, 1.000)])
    """参数:
        - change_voice_param_pitch: 默认0.83, 0.00 ~ 1.00
        - change_voice_param_timbre: 默认1.00, 0.00 ~ 1.00
    """

class CapCutVoiceCharactersEffectType(EffectEnum):
    """CapCut自带的Voice characters特效类型"""

    Fussy_male   = EffectMeta("Fussy male", False, "7337197310696231425", "00C65F8A-44A7-4B17-8F39-93464E72823D", "", [])
    Bestie       = EffectMeta("Bestie", False, "7252272084292735489", "B9B3885C-BF7D-4B5C-9545-B0CD3218F292", "", [])
    Queen        = EffectMeta("Queen", False, "7337197136242545153", "17A7F413-C044-4F1F-9644-1337686BE406", "", [])
    Squirrel     = EffectMeta("Squirrel", False, "7338257533796094466", "76668599-E132-42DF-99F8-6F086B3B56E9", "b2b3f551b703c87e8e057ad8f92fafbb", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
        - strength: 默认1.00, 0.00 ~ 1.00
    """
    Distorted    = EffectMeta("Distorted", False, "7021052602091573761", "F995614C-D100-481D-A708-59829794EF3E", "ce0bc10d76e22a718094c152f7beae25", [
                              EffectParam("change_voice_param_pitch", 0.650, 0.000, 1.000),
                              EffectParam("change_voice_param_timbre", 0.780, 0.000, 1.000)])
    """参数:
        - change_voice_param_pitch: 默认0.65, 0.00 ~ 1.00
        - change_voice_param_timbre: 默认0.78, 0.00 ~ 1.00
    """
    Chipmunk     = EffectMeta("Chipmunk", False, "7021052742021943810", "B5C8BB3C-7765-4572-B8B9-9071A903D899", "4ff3edc0229bfac112c1caefe75e7039", [
                              EffectParam("change_voice_param_pitch", 0.500, 0.000, 1.000),
                              EffectParam("change_voice_param_timbre", 0.500, 0.000, 1.000)])
    """参数:
        - change_voice_param_pitch: 默认0.50, 0.00 ~ 1.00
        - change_voice_param_timbre: 默认0.50, 0.00 ~ 1.00
    """
    Trickster    = EffectMeta("Trickster", False, "7254407946195440130", "11F394B0-E601-4DD5-BBEA-76A8CADE222A", "8dd8889045e6c065177df791ddb3dfb8", [])
    Elf          = EffectMeta("Elf", False, "7021052754512581122", "EF781DEC-265B-4B6D-A68E-5EDC75DDCA84", "bbf0f0d1532a249e9a1f7f3444e1e437", [
                              EffectParam("change_voice_param_pitch", 0.750, 0.000, 1.000),
                              EffectParam("change_voice_param_timbre", 0.600, 0.000, 1.000)])
    """参数:
        - change_voice_param_pitch: 默认0.75, 0.00 ~ 1.00
        - change_voice_param_timbre: 默认0.60, 0.00 ~ 1.00
    """
    Elfy         = EffectMeta("Elfy", False, "7311544785477571074", "58E4D6DE-5D7A-42C8-BE16-1AFF43666512", "8dd8889045e6c065177df791ddb3dfb8", [])
    Santa        = EffectMeta("Santa", False, "7311544442723242497", "8E8A0DA9-1267-41E6-AFA4-20B2A4171BA4", "8dd8889045e6c065177df791ddb3dfb8", [])
    Jessie       = EffectMeta("Jessie", False, "7254408415026352642", "F3EBF9DB-195D-4531-94A8-F52964DB0C83", "8dd8889045e6c065177df791ddb3dfb8", [])
    Good_Guy     = EffectMeta("Good Guy", False, "7259231960889823746", "27D9D7EC-BFF2-4481-92D0-40E3CBF9C2FB", "8dd8889045e6c065177df791ddb3dfb8", [])
    Robot        = EffectMeta("Robot", False, "7021052669863137794", "DD71C5CB-683A-4FFA-BEAA-33D568333486", "123114835bda73b8de4aa106ccde0bb2", [
                              EffectParam("change_voice_param_strength", 1.000, 0.000, 1.000)])
    """参数:
        - change_voice_param_strength: 默认1.00, 0.00 ~ 1.00
    """

class CapCutSpeechToSongEffectType(EffectEnum):
    """CapCut自带的Speech to song特效类型"""

    Folk         = EffectMeta("Folk", False, "7413437147539164421", "9A9C3804-5241-44E9-AF56-1BE8271083F2", "", [])

