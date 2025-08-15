

from .effect_meta import EffectEnum
from .effect_meta import EffectMeta, EffectParam

class CapCutVideoSceneEffectType(EffectEnum):
    """CapCut自带的画面特效类型"""

    Blur         = EffectMeta("Blur", False, "6739752823140913675", "15206412", "2db7bf49d9349e308ef0f46c39b14abf", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    Fade_In      = EffectMeta("Fade In", False, "6722343568188379661", "15206270", "a299b022ab4d7a1830ac72dce3d21d95", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Heart_Kisses = EffectMeta("Heart Kisses", False, "6925620336390050305", "15207108", "dce0f289716b6e4c4c7256a4ab364188", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Explosion    = EffectMeta("Explosion", False, "6740540228194275844", "15206955", "b368d3f6335a5880ecc1c69c3d805cc3", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Fireworks_2  = EffectMeta("Fireworks 2", False, "6767147410671014407", "15207172", "7eed03f0203ac3c7dad4a60b433b8af3", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Fade_Out     = EffectMeta("Fade Out", False, "6723050814006366734", "15206256", "05c17ac3298c0521cd91a720850a27de", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    The_End      = EffectMeta("The End", False, "6710109932122804750", "15206257", "24749b428adbacfa9712b8a249912905", [])
    Zoom_Lens    = EffectMeta("Zoom Lens", False, "6868546663607177736", "15206420", "6f7b76eec49d46f9397eafb4980a17d4", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.30, 0.00 ~ 1.00
    """
    Meteor       = EffectMeta("Meteor", False, "6808838081420988942", "15206953", "3caa2d665bc97ae2956e1130f6a4db6a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Horizontal_Open = EffectMeta("Horizontal Open", False, "6706773534074491403", "15206251", "dc2ce1b151dd2e4dead3333902cb5afa", [])
    Spectrum_Scan = EffectMeta("Spectrum Scan", False, "7257406643984404993", "51063478", "6d8fcac7a573c8ff756f131034946db5", [
                              EffectParam("effects_adjust_background_animation", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.614, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.642, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.61, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.64, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.33, 0.00 ~ 1.00
    """
    By_the_Fireplace = EffectMeta("By the Fireplace", False, "7116775483395543554", "15206952", "6422961dbe02f34709668b2f7cac5ea7", [
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.20, 0.00 ~ 1.00
        - sticker: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.40, 0.00 ~ 1.00
    """
    Rolling_Film = EffectMeta("Rolling Film", False, "7088226690396066305", "15206743", "19151c1293399104b1aed93d36427182", [
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
    """
    Landscape_Close = EffectMeta("Landscape Close", False, "6876378886859395585", "15206255", "b7abe840af4f942b11e0ccda971d4df7", [])
    Flipped      = EffectMeta("Flipped", False, "6925617622302069250", "15207107", "d5e216a1700db22637509d2966004b16", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Horizontal_Close = EffectMeta("Horizontal Close", False, "6725685146323784205", "15206265", "93a3a5fbe5f3b343667f7affe22b97f9", [])
    Astral       = EffectMeta("Astral", False, "6706773500784284172", "15206576", "8f93377f4a87f0075c796732598f133a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
    """
    Edge_Glow    = EffectMeta("Edge Glow", False, "6769065553207235086", "15206415", "9768e7f5b5d8c89e82cf4ebd80768263", [
                              EffectParam("effects_adjust_luminance", 0.250, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.25, 0.00 ~ 1.00
    """
    Shake        = EffectMeta("Shake", False, "6761645818723176968", "739328", "d11532bfbfbd6f9af59026c2c42f2570", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
    """
    Camera_Focus = EffectMeta("Camera Focus", False, "6719658716750156291", "15206267", "feb43ab124f2c4bc8ee045a773741ed9", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.250, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.25, 0.00 ~ 1.00
    """
    Collision_Sparks = EffectMeta("Collision Sparks", False, "6975124370003857921", "15206948", "7ba6614d70f2265795265e102d049d7a", [])
    Diamond_Zoom = EffectMeta("Diamond Zoom", False, "7148318643170841090", "15206248", "fda851ab65ee2b7bd6bb568a0e8bc544", [
                              EffectParam("effects_adjust_size", 0.521, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.720, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.52, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.72, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.50, 0.00 ~ 1.00
    """
    Disco_Ball_1 = EffectMeta("Disco Ball 1", False, "6771299914891661832", "15206551", "ac75bc8cb54c6cf163065a31d4d6732b", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Mini_Zoom    = EffectMeta("Mini Zoom", False, "6791743223522923021", "15206419", "c09004507723569a3e762494d4ffda7d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
    """
    Bluray_Scanning = EffectMeta("Blu-ray Scanning", False, "7255269076526699010", "51063477", "5f9918f9606b3dfbb8e8c8b7b90ca0e3", [
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.70, 0.00 ~ 1.00
    """
    Portrait_Open = EffectMeta("Portrait Open", False, "6876379009664422402", "15206269", "d75e138469226782f6d918983725d700", [])
    Girls_Secrets = EffectMeta("Girl's Secrets", False, "6925618573083677185", "15207106", "ebba75bb53013a6347814b486c6063eb", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    Color_Phosphor = EffectMeta("Color Phosphor", False, "6972419670712259074", "15206552", "6a50bf39711faf7b7f94bf68fed7a33f", [])
    Rebound_Swing = EffectMeta("Rebound Swing", False, "7174685191602967041", "15206538", "00cb18af745bc30702d78b9dae914465", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.00, 0.00 ~ 1.00
    """
    Camera_Shake = EffectMeta("Camera Shake", False, "6863326875649839623", "15206571", "7cb6c1646c43d86a394245e194e3f451", [
                              EffectParam("effects_adjust_range", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Pulse        = EffectMeta("Pulse", False, "6723068356821258764", "15206564", "83aa305dcf2f6f4890efaca2546c4463", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Vertical_Open = EffectMeta("Vertical Open", False, "6708899027976458760", "15206263", "be40f98619f47a8535158e873b273cce", [])
    Star         = EffectMeta("Star", False, "6946490242190807553", "15206658", "3c8c6e57ebbcca08e0202a2ce489a109", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    Heart_Disco  = EffectMeta("Heart Disco", False, "7042563282523132417", "15206540", "076a41421bbc4a6419fcccdc3c1ce80c", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.634, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.63, 0.00 ~ 1.00
    """
    Butterfly_Dream = EffectMeta("Butterfly Dream", False, "7013301550458081794", "15206963", "f6829a9af2cd1b32e1aac84543e0931b", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Camcorder    = EffectMeta("Camcorder", False, "6723065859260027403", "15207075", "f05977a18144296bdfa45ca3493d84a9", [])
    TV_On        = EffectMeta("TV On", False, "6719661856434164237", "15206258", "b7f303766220a86078204b79a4db2566", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.60, 0.00 ~ 1.00
    """
    Vignette     = EffectMeta("Vignette", False, "6723086142658318860", "15206403", "ef7abad9671e2f3da7993b7673ece5fc", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    Heartbeat    = EffectMeta("Heartbeat", False, "6746014633942848007", "15207097", "6d42bba28607f45ca90a7359b7c6ab74", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Blurry_Focus = EffectMeta("Blurry Focus", False, "6758752103092457991", "15206250", "5dd4bf7e879fe7356e3e27e5105f5af1", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.250, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.25, 0.00 ~ 1.00
    """
    Noise_2      = EffectMeta("Noise 2", False, "6803161742789579277", "15206730", "53ff3188476c74715a73aa34f08a1edf", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Leak_1       = EffectMeta("Leak 1", False, "6815093106841489934", "15206864", "97fea18d6a469abd49e3f1d28628e61f", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Black_Noise  = EffectMeta("Black Noise", False, "6888643828492800514", "15206732", "e7baebcf969437d4d5cdb607578bbf89", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Old_TV_2     = EffectMeta("Old TV 2", False, "6865921078858879496", "15206785", "62b508cb16fd1c0da7a2989da5bd49fd", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Fuzzy        = EffectMeta("Fuzzy", False, "6709706457543086605", "15206813", "467d4eff311315de8fa6549625919286", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    Soft         = EffectMeta("Soft", False, "6706773499836371463", "15206402", "258b5bd7ba1fb94dce800bc496a30ed9", [
                              EffectParam("effects_adjust_soft", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_soft: 默认0.70, 0.00 ~ 1.00
    """
    TV_Off       = EffectMeta("TV Off", False, "6719656840646365707", "15206261", "c2ef989d8286f4b2e5a747bca129602a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.60, 0.00 ~ 1.00
    """
    Lightning_Crack = EffectMeta("Lightning Crack", False, "7111576355736654337", "15207138", "edd537366858130e593a074d28503dc7", [
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.800, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.80, 0.00 ~ 1.00
        - sticker: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
    """
    Shake_3      = EffectMeta("Shake 3", False, "6706773500796867084", "15206559", "950894d4ae28d859d9b7136a73265ee6", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.750, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.75, 0.00 ~ 1.00
    """
    Gleam        = EffectMeta("Gleam", False, "7176638378056618497", "15206657", "af6015fc0590a70892d5084082fd4490", [
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_soft: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    Butterflies  = EffectMeta("Butterflies", False, "6748307256959308299", "15206962", "45377639fc1c0b29cc889f71f6ca2fd0", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Ripple       = EffectMeta("Ripple", False, "7173547719485559298", "15206680", "c0db14b731d4f04c95332348a0488089", [
                              EffectParam("effects_adjust_sharpen", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.550, 0.000, 1.000)])
    """参数:
        - effects_adjust_sharpen: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.55, 0.00 ~ 1.00
    """
    Electro_Border = EffectMeta("Electro Border", False, "7081821838967312898", "15206951", "15153b69c032c89f4087d12ef7a613ca", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.50, 0.00 ~ 1.00
    """
    Shake_1      = EffectMeta("Shake", False, "6709706542674874888", "15206579", "bb8e9483313416d32bea215d57855490", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
    """
    Trilayer_Mirror = EffectMeta("Tri-layer Mirror", False, "7134537649410281985", "15207281", "26e730a32387f88e9a67c4e8213d9920", [
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    Radiating_Love = EffectMeta("Radiating Love", False, "7058919485918417409", "15207096", "cbf62902df7101761116f28616cbbabc", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    White_Flash  = EffectMeta("White Flash", False, "6706773500792672781", "15206539", "f0804cb2cb4e88a036ecf87dcf031cf0", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Lightning    = EffectMeta("Lightning", False, "7104581530567053825", "15207206", "a13ca8bfd8348a04e8d170d16ec8ed16", [
                              EffectParam("effects_adjust_color", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 1.000, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认1.00, 0.00 ~ 1.00
        - sticker: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    Motion_Blur  = EffectMeta("Motion Blur", False, "7011333202614686210", "15206399", "167deb8c5b35d5a3097cb107693c62c3", [
                              EffectParam("effects_adjust_horizontal_shift", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.850, 0.000, 1.000)])
    """参数:
        - effects_adjust_horizontal_shift: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.85, 0.00 ~ 1.00
    """
    Spooky_Camera = EffectMeta("Spooky Camera", False, "7289325398410662401", "103412411", "2c2c06b5bfa714e7dea247d5200d1513", [
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.800, 0.000, 1.000),
                              EffectParam("sticker", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.80, 0.00 ~ 1.00
        - sticker: 默认0.40, 0.00 ~ 1.00
    """
    Frosted_Quality = EffectMeta("Frosted Quality", False, "7137191291334431234", "15206724", "fbdce889885763ee82ffa7138de4d36b", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.50, 0.00 ~ 1.00
    """
    Frosted_Quality_1 = EffectMeta("Frosted Quality", False, "7137191291334431234", "3330082", "fbdce889885763ee82ffa7138de4d36b", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.50, 0.00 ~ 1.00
    """
    Leak_2       = EffectMeta("Leak 2", False, "6814743838964322829", "15206869", "7b4f9381351d3e703cd06e95ab3a9b06", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Vertical_Close = EffectMeta("Vertical Close", False, "6729065630013592067", "15206266", "5653f70097408fcbcbe82af864d70b13", [])
    Rainbow_Neon = EffectMeta("Rainbow Neon", False, "7197323104480137729", "12379624", "7a21f2671042a6e902620edf09a59093", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.120, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.200, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.12, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.20, 0.00 ~ 1.00
    """
    Sharpen_Edges = EffectMeta("Sharpen Edges", False, "7288638980797501954", "104621958", "df34b01300ddefbfd8b04bee900ae432", [
                              EffectParam("effects_adjust_blur", 0.120, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.080, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.12, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.08, 0.00 ~ 1.00
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
    """
    Chromatic    = EffectMeta("Chromatic", False, "6709347834690277892", "15206809", "34c4ef20e2bbbc8e16e051ed901c387d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
    """
    Dizzy        = EffectMeta("Dizzy", False, "7174360485435806210", "6518697", "ab6aa4d420ef1cf322d25b24a054a7c6", [
                              EffectParam("effects_adjust_size", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.900, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.90, 0.00 ~ 1.00
    """
    Swing        = EffectMeta("Swing", False, "7389178610755572225", "397260584", "bee293df8d3c2a62e722c60eca82aab3", [])
    Halo_2       = EffectMeta("Halo 2", False, "6709701759398318604", "15206860", "63cf76363a869a8e0134f9dc6212957c", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Leak_2_1     = EffectMeta("Leak 2", False, "7190317638709416449", "9361407", "544b2c0bf76efcafa4c17a7656504262", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.470, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.47, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    Vertical_Blur = EffectMeta("Vertical Blur", False, "6716684911840858628", "15206268", "301f4e40cf408cb323fca377af84f18e", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    Black_Flash  = EffectMeta("Black Flash", False, "6863327462470717960", "15206545", "383b8ace93434f0c5d17689933140422", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Wipe_Board   = EffectMeta("Wipe Board", False, "6841459176510591496", "15206259", "6725bf6b227fc208a7bd343661637320", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Butterfly_Color = EffectMeta("Butterfly Color", False, "6972511965025407490", "15206960", "aaabe838a4c6a61d6018002854acbc6d", [])
    Camera_Focus_2 = EffectMeta("Camera Focus 2", False, "6969074495533355521", "15206253", "742d42af866aa0dad5e9029ff692a269", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    To_Color     = EffectMeta("To Color", False, "6720492336788279815", "15206260", "0178a55e4f8c7deec8786d78d875d45e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Flicker      = EffectMeta("Flicker", False, "6717639344577843725", "15206570", "0bc9ee34335ba4f9d75e4a2b21f4d6e5", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Pixel_Blur   = EffectMeta("Pixel Blur", False, "6730841158806671886", "15206262", "c16410155f6fe0fbac8d4a58c06df3ca", [
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_noise: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    TV_Colored_Lines = EffectMeta("TV Colored Lines", False, "6852503085672043021", "15206778", "d6ef86b7e37c1996e336d6541f5c4d7a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    Shake_2      = EffectMeta("Shake 2", False, "6821460674577699342", "15206578", "332436443a8cbe9014d6bf7c8531ff60", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
    """
    Wobbly_Black = EffectMeta("Wobbly Black", False, "6865921530488951309", "15207069", "2457889e649132e1a427ccd9c258e51e", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Strobe       = EffectMeta("Strobe", False, "6716419849544798723", "15206565", "c5bed1ab7aee34bfb9b3c6ab3705eb28", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
    """
    Fade_In_1    = EffectMeta("Fade In", False, "6722343568188379661", "15206270", "a299b022ab4d7a1830ac72dce3d21d95", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Fade_In_2    = EffectMeta("Fade In", False, "6722343568188379661", "15206270", "a299b022ab4d7a1830ac72dce3d21d95", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Fade_Out_1   = EffectMeta("Fade Out", False, "6723050814006366734", "15206256", "05c17ac3298c0521cd91a720850a27de", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    The_End_1    = EffectMeta("The End", False, "6710109932122804750", "15206257", "24749b428adbacfa9712b8a249912905", [])
    Horizontal_Open_1 = EffectMeta("Horizontal Open", False, "6706773534074491403", "15206251", "dc2ce1b151dd2e4dead3333902cb5afa", [])
    Blurry_Focus_1 = EffectMeta("Blurry Focus", False, "6758752103092457991", "15206250", "5dd4bf7e879fe7356e3e27e5105f5af1", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.250, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.25, 0.00 ~ 1.00
    """
    Diamond_Zoom_1 = EffectMeta("Diamond Zoom", False, "7148318643170841090", "15206248", "fda851ab65ee2b7bd6bb568a0e8bc544", [
                              EffectParam("effects_adjust_size", 0.521, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.720, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.52, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.72, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.50, 0.00 ~ 1.00
    """
    Horizontal_Close_1 = EffectMeta("Horizontal Close", False, "6725685146323784205", "15206265", "93a3a5fbe5f3b343667f7affe22b97f9", [])
    Landscape_Close_1 = EffectMeta("Landscape Close", False, "6876378886859395585", "15206255", "b7abe840af4f942b11e0ccda971d4df7", [])
    Vertical_Open_1 = EffectMeta("Vertical Open", False, "6708899027976458760", "15206263", "be40f98619f47a8535158e873b273cce", [])
    Camera_Focus_1 = EffectMeta("Camera Focus", False, "6719658716750156291", "15206267", "feb43ab124f2c4bc8ee045a773741ed9", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.250, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.25, 0.00 ~ 1.00
    """
    Portrait_Open_1 = EffectMeta("Portrait Open", False, "6876379009664422402", "15206269", "d75e138469226782f6d918983725d700", [])
    TV_Off_1     = EffectMeta("TV Off", False, "6719656840646365707", "15206261", "c2ef989d8286f4b2e5a747bca129602a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.60, 0.00 ~ 1.00
    """
    Camera_Focus_2_1 = EffectMeta("Camera Focus 2", False, "6969074495533355521", "15206253", "742d42af866aa0dad5e9029ff692a269", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    Vertical_Close_1 = EffectMeta("Vertical Close", False, "6729065630013592067", "15206266", "5653f70097408fcbcbe82af864d70b13", [])
    TV_On_1      = EffectMeta("TV On", False, "6719661856434164237", "15206258", "b7f303766220a86078204b79a4db2566", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.60, 0.00 ~ 1.00
    """
    Low_Exposure = EffectMeta("Low Exposure", False, "6765766949382132232", "15206254", "be1c0676764ee83d32b63afc46272c28", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    To_Color_1   = EffectMeta("To Color", False, "6720492336788279815", "15206260", "0178a55e4f8c7deec8786d78d875d45e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Wipe_Board_1 = EffectMeta("Wipe Board", False, "6841459176510591496", "15206259", "6725bf6b227fc208a7bd343661637320", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Vertical_Blur_1 = EffectMeta("Vertical Blur", False, "6716684911840858628", "15206268", "301f4e40cf408cb323fca377af84f18e", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    White_Out    = EffectMeta("White Out", False, "6723790385069429262", "15206264", "94b1df840d30218f14e8a5e509df5c8e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Rebound_Swing_1 = EffectMeta("Rebound Swing", False, "7174685191602967041", "15206538", "00cb18af745bc30702d78b9dae914465", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.00, 0.00 ~ 1.00
    """
    Astral_1     = EffectMeta("Astral", False, "6706773500784284172", "15206576", "8f93377f4a87f0075c796732598f133a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
    """
    Disco_Ball_1_1 = EffectMeta("Disco Ball 1", False, "6771299914891661832", "15206551", "ac75bc8cb54c6cf163065a31d4d6732b", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Color_Phosphor_1 = EffectMeta("Color Phosphor", False, "6972419670712259074", "15206552", "6a50bf39711faf7b7f94bf68fed7a33f", [])
    Camera_Shake_1 = EffectMeta("Camera Shake", False, "6863326875649839623", "15206571", "7cb6c1646c43d86a394245e194e3f451", [
                              EffectParam("effects_adjust_range", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Pulse_1      = EffectMeta("Pulse", False, "6723068356821258764", "15206564", "83aa305dcf2f6f4890efaca2546c4463", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Shake_4      = EffectMeta("Shake", False, "6761645818723176968", "739328", "d11532bfbfbd6f9af59026c2c42f2570", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
    """
    Shockwave    = EffectMeta("Shockwave", False, "6968382387759616514", "15206562", "ad8e0a154e7a3c78dc23407ec23da9b2", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Heart_Disco_1 = EffectMeta("Heart Disco", False, "7042563282523132417", "15206540", "076a41421bbc4a6419fcccdc3c1ce80c", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.634, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.63, 0.00 ~ 1.00
    """
    Shake_3_1    = EffectMeta("Shake 3", False, "6706773500796867084", "15206559", "950894d4ae28d859d9b7136a73265ee6", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.750, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.75, 0.00 ~ 1.00
    """
    Black_Flash_2 = EffectMeta("Black Flash 2", False, "7159482508998873601", "4780027", "3c25ccac35121fe42e647b119e37a21f", [
                              EffectParam("effects_adjust_speed", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.40, 0.00 ~ 1.00
    """
    Throb        = EffectMeta("Throb", False, "7052996558211518977", "15206558", "c65fc5a267dde559e80e16c8fcc9cd6c", [
                              EffectParam("effects_adjust_luminance", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.70, 0.00 ~ 1.00
    """
    Strobe_1     = EffectMeta("Strobe", False, "6716419849544798723", "15206565", "c5bed1ab7aee34bfb9b3c6ab3705eb28", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
    """
    Shake_5      = EffectMeta("Shake", False, "6709706542674874888", "15206579", "bb8e9483313416d32bea215d57855490", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
    """
    White_Flash_1 = EffectMeta("White Flash", False, "6706773500792672781", "15206539", "f0804cb2cb4e88a036ecf87dcf031cf0", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Flicker_1    = EffectMeta("Flicker", False, "6717639344577843725", "15206570", "0bc9ee34335ba4f9d75e4a2b21f4d6e5", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Colorful     = EffectMeta("Colorful", False, "6758298031608566280", "15206575", "51b2af1e78502e00abb3d47b21a55796", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    Club_Mood    = EffectMeta("Club Mood", False, "6926449541159850498", "15206542", "3bb76ef02392a04f5b387dbd46942458", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    Neon_Outline = EffectMeta("Neon Outline", False, "6904545068309287425", "15206554", "49db41dc5ace9aa5478f46c7beb9559b", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    RGB_Border   = EffectMeta("RGB Border", False, "6922702317225513474", "15206560", "175536eb523aae867ae4b8cb94f09211", [
                              EffectParam("effects_adjust_speed", 0.670, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.67, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    Black_Flash_1 = EffectMeta("Black Flash", False, "6863327462470717960", "15206545", "383b8ace93434f0c5d17689933140422", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Blur_1       = EffectMeta("Blur", False, "6904544739727512065", "15206553", "6decf1b703bdfdfaac0d6f6f9b14594f", [
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
    """
    Disco        = EffectMeta("Disco", False, "6716450942285255182", "15206567", "355d46c4bff8c9b6286f3324fb6e27b7", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Delay        = EffectMeta("Delay", False, "6706773549362713095", "15206569", "7c2f3180ded615ee30e6d1a5bafc5392", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
    """
    Neon_Swing   = EffectMeta("Neon Swing", False, "6926406957624463873", "15206537", "ead112f7fba9cc2c2a448ebcc028b4a7", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认1.00, 0.00 ~ 1.00
    """
    Shadow       = EffectMeta("Shadow", False, "6766876614862049795", "15206536", "f97bd68cfc43174bcb30406a6fc46952", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
    """
    Color_Flame  = EffectMeta("Color Flame", False, "6967303566226625026", "15206555", "2a83206eb7f6f9d65af177a29ea223e2", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    Rainbow_Haze = EffectMeta("Rainbow Haze", False, "6756845151630397960", "15206535", "a5f61f00265cbcf6fbc430780f5b4c03", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    Unreal       = EffectMeta("Unreal", False, "6723059630676644364", "15206557", "44cb0b2f810fa3119f2c9f1ae396db9d", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
    """
    Flashing_Frame = EffectMeta("Flashing Frame", False, "7003233732018573826", "15206541", "d3c2769c454f504272e2b5a1b96b5a61", [
                              EffectParam("effects_adjust_speed", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    Trippy       = EffectMeta("Trippy", False, "6709706311455478285", "15206561", "81244293ba7904eda4db87d1f8c59674", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    Orange_Negative = EffectMeta("Orange Negative", False, "6915344828905558530", "15206563", "95ddc63de88b65e1782c88c300c7e90e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    White_Border = EffectMeta("White Border", False, "6954296354319372802", "15206544", "647776c50dafcbfab55f1dcb36d28792", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    Color_Negative = EffectMeta("Color Negative", False, "6915344758177010177", "15206573", "a78b49205a5d3b7fbc04a19aebce80ea", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    Stuck_Frame  = EffectMeta("Stuck Frame", False, "7046749941888193025", "15206548", "ea84ea931c93434b86263b92aabbadd4", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Zoom_Lens_1  = EffectMeta("Zoom Lens", False, "6868546663607177736", "15206420", "6f7b76eec49d46f9397eafb4980a17d4", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.300, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.30, 0.00 ~ 1.00
    """
    Mini_Zoom_1  = EffectMeta("Mini Zoom", False, "6791743223522923021", "15206419", "c09004507723569a3e762494d4ffda7d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
    """
    Magnifying_Glass = EffectMeta("Magnifying Glass", False, "7053030891085369858", "15207071", "5f89a973e9cea025690bdb37a293a959", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
    """
    Wide_Angle   = EffectMeta("Wide Angle", False, "7090878082784956930", "15206406", "17c3a4c4b6664d247c90a6e1bda8e6dd", [
                              EffectParam("effects_adjust_intensity", 0.450, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.45, 0.00 ~ 1.00
    """
    Heart_Magnifier = EffectMeta("Heart Magnifier", False, "7079996857874649601", "15207067", "2f62bf787eb44535dbd128d60f46a29c", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.00, 0.00 ~ 1.00
    """
    Chrome_Blur  = EffectMeta("Chrome Blur", False, "6716422405511713287", "15206410", "53c8584c8174f887b2802540dd28955b", [
                              EffectParam("effects_adjust_blur", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.550, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.55, 0.00 ~ 1.00
    """
    Fisheye_4    = EffectMeta("Fisheye 4", False, "7091907591374115330", "15206409", "ae54d40500bd55859922c0afaf05d42c", [
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.550, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.55, 0.00 ~ 1.00
    """
    Swing_1      = EffectMeta("Swing", False, "7389178610755572225", "397260584", "bee293df8d3c2a62e722c60eca82aab3", [])
    Cinema       = EffectMeta("Cinema", False, "6719333680713568771", "15206416", "20175443ac3ff3f77c48019889186568", [])
    Rotary_Focus = EffectMeta("Rotary Focus", False, "7221462783739564546", "26123989", "ee5c7f8a1180bd5d8e0d4da0357e8d99", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Blink        = EffectMeta("Blink", False, "6752780026900386317", "15206418", "c742af6913646f7c936642aae51d58d2", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Chromatic_Quirk = EffectMeta("Chromatic Quirk", False, "6706773498561303044", "15206400", "737c54ea0dcf628cc78714a77eef52a3", [
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    Backlit_Focus = EffectMeta("Backlit Focus", False, "6995058478553240065", "15206405", "ccba5bb5c3656e951ce7e6ec272dc606", [
                              EffectParam("effects_adjust_soft", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_soft: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.33, 0.00 ~ 1.00
    """
    Hazy         = EffectMeta("Hazy", False, "6756397840785740295", "15206408", "d022f68235da2c057cb3aa2495fb249c", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    Blackout     = EffectMeta("Blackout", False, "7244440311160640002", "37784032", "a1a88c0fa966966cbe13373ad2b7382d", [
                              EffectParam("effects_adjust_blur", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.80, 0.00 ~ 1.00
    """
    Mirror       = EffectMeta("Mirror", False, "6956418086534648321", "15206407", "0e68989382af0ece7e1e864cc2107c67", [])
    Fisheye      = EffectMeta("Fisheye", False, "6867722963865571854", "15206401", "d577e4744d29d971675ec9c71d94ca94", [
                              EffectParam("effects_adjust_distortion", 0.770, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认0.77, 0.00 ~ 1.00
    """
    Fisheye_2    = EffectMeta("Fisheye 2", False, "7024057726879666690", "15206413", "3961e7c38420d89d64c5d267a3068254", [
                              EffectParam("effects_adjust_speed", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.80, 0.00 ~ 1.00
    """
    VX1000       = EffectMeta("VX1000", False, "7236337500162101762", "34612927", "8e488631140f60f94e3bf0875d538858", [
                              EffectParam("effects_adjust_distortion", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.200, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.20, 0.00 ~ 1.00
    """
    Binoculars   = EffectMeta("Binoculars", False, "6834012604759806472", "15206417", "63e50736865f6248f87b6280c5b0d88b", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Spectrum_Scan_1 = EffectMeta("Spectrum Scan", False, "7257406643984404993", "51063478", "6d8fcac7a573c8ff756f131034946db5", [
                              EffectParam("effects_adjust_background_animation", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.614, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.642, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.61, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.64, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.33, 0.00 ~ 1.00
    """
    Explosion_1  = EffectMeta("Explosion", False, "6740540228194275844", "15206955", "b368d3f6335a5880ecc1c69c3d805cc3", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Tree_Shade   = EffectMeta("Tree Shade", False, "6815830852035940872", "15206872", "e94e1952adee72678c426490036dae61", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    By_the_Fireplace_1 = EffectMeta("By the Fireplace", False, "7116775483395543554", "15206952", "6422961dbe02f34709668b2f7cac5ea7", [
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.20, 0.00 ~ 1.00
        - sticker: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.40, 0.00 ~ 1.00
    """
    Leak_1_1     = EffectMeta("Leak 1", False, "6815093106841489934", "15206864", "97fea18d6a469abd49e3f1d28628e61f", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Angel        = EffectMeta("Angel", False, "6721949326022545928", "15206867", "37c4098ac98fc25188a5a727064a7729", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    Sunset_4     = EffectMeta("Sunset 4", False, "6834008866137575950", "15206861", "858aa00b8938e4f0dde79225ef119f60", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Spark        = EffectMeta("Spark", False, "6715209198109463054", "15206947", "e1f99bc44e7da14483e58a762a1bcbd2", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Meteor_1     = EffectMeta("Meteor", False, "6808838081420988942", "15206953", "3caa2d665bc97ae2956e1130f6a4db6a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Bluray_Scanning_1 = EffectMeta("Blu-ray Scanning", False, "7255269076526699010", "51063477", "5f9918f9606b3dfbb8e8c8b7b90ca0e3", [
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.70, 0.00 ~ 1.00
    """
    Leak_2_2     = EffectMeta("Leak 2", False, "6814743838964322829", "15206869", "7b4f9381351d3e703cd06e95ab3a9b06", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Dizzy_1      = EffectMeta("Dizzy", False, "7174360485435806210", "6518697", "ab6aa4d420ef1cf322d25b24a054a7c6", [
                              EffectParam("effects_adjust_size", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.900, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.90, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.90, 0.00 ~ 1.00
    """
    Collision_Sparks_1 = EffectMeta("Collision Sparks", False, "6975124370003857921", "15206948", "7ba6614d70f2265795265e102d049d7a", [])
    Spark_2      = EffectMeta("Spark 2", False, "6907199041285657089", "15206950", "43a04949ebd13d27d7b38f5083882322", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Pool_Reflection = EffectMeta("Pool Reflection", False, "7123129087895278081", "15206873", "0e8f5cf28c600c62140c2f3666dbe18b", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.150, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.15, 0.00 ~ 1.00
    """
    Magic        = EffectMeta("Magic", False, "7024492507387924993", "15207014", "98296a4bc028cef2bb3b06ffbb490faf", [
                              EffectParam("effects_adjust_speed", 0.336, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.802, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Blinds_2     = EffectMeta("Blinds 2", False, "6823656768334205454", "15206874", "380df1dbfbfb93a560b389d5683043e7", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Negative_Strobe = EffectMeta("Negative Strobe", False, "7154203775824040450", "15207011", "c737112d913d14f6cc8871dbc51c8013", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.850, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.85, 0.00 ~ 1.00
    """
    Negative_Strobe_1 = EffectMeta("Negative Strobe", False, "7154203775824040450", "4278136", "c737112d913d14f6cc8871dbc51c8013", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.850, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.45, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.85, 0.00 ~ 1.00
    """
    Halo         = EffectMeta("Halo", False, "6714239617916211716", "15206863", "5dd6c29087b42206d70da0d13d4b7251", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Rainbow_Sparkle = EffectMeta("Rainbow Sparkle", False, "6717434470128947725", "15206870", "ae2e32daa7af0fa8f4b61a0c5aacd196", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    Tree_Shade_2 = EffectMeta("Tree Shade 2", False, "6820591707617235464", "15206868", "068b6e28050ccaa8d0832419a0a185c4", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Halo_2_1     = EffectMeta("Halo 2", False, "6709701759398318604", "15206860", "63cf76363a869a8e0134f9dc6212957c", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Light_leak   = EffectMeta("Light leak", False, "6810944598874001934", "15206876", "e8d86b0790f9e125d208d874fe97c9e0", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    Window       = EffectMeta("Window", False, "6823659309428118030", "15206875", "6bd27e2b68879bb788d7ef0265648795", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Flash        = EffectMeta("Flash", False, "6844432942563856904", "15206866", "c602afac7537de506bb822c37e9f2191", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Blinds       = EffectMeta("Blinds", False, "6823654892872143367", "15206862", "bde8d2cb9d033a45c92615f9b18b47a1", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Flame_Frame  = EffectMeta("Flame Frame", False, "7135324113551233537", "15206949", "bd65acfadb0b7613c33100fa63abcf5e", [
                              EffectParam("effects_adjust_color", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
    """
    Cold_Lab     = EffectMeta("Cold Lab", False, "7021892814455706113", "15207023", "0ba96868fd684b80b4cb82f058f35dc9", [
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.267, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.27, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Glowburst    = EffectMeta("Glowburst", False, "6753169731617821191", "15206859", "d7c42c303074967c0cad7c7a6adfe896", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Electro_Heart = EffectMeta("Electro Heart", False, "7091926525108294145", "15206954", "04883bbcc4ce20a240d5f90dc34db76f", [
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.419, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.473, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.590, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.42, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.47, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.59, 0.00 ~ 1.00
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认1.00, 0.00 ~ 1.00
    """
    Develop      = EffectMeta("Develop", False, "6830336944111620616", "15206877", "a09195689037df58fd23db7f28d3a2b6", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_soft: 默认1.00, 0.00 ~ 1.00
    """
    Electro_Border_1 = EffectMeta("Electro Border", False, "7081821838967312898", "15206951", "15153b69c032c89f4087d12ef7a613ca", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.50, 0.00 ~ 1.00
    """
    Train_Window = EffectMeta("Train Window", False, "6834006887415943694", "15206871", "d37540d91f173eaeef40a3ac6a2de42e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Film_Frame   = EffectMeta("Film Frame", False, "7008413768564609538", "15206745", "d5f6e3f656074eaaaad12544b43dee93", [])
    Dark_Night   = EffectMeta("Dark Night", False, "6887445808078131714", "15207006", "17b5b34a9580eca1b093e3b9b730b5ad", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
    """
    Noise_1      = EffectMeta("Noise 1", False, "6706773534066086413", "15206735", "f090492c306fe35f917eed1216f14f8c", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Noise_2_1    = EffectMeta("Noise 2", False, "6803161742789579277", "15206730", "53ff3188476c74715a73aa34f08a1edf", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Black_Noise_1 = EffectMeta("Black Noise", False, "6888643828492800514", "15206732", "e7baebcf969437d4d5cdb607578bbf89", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Retro_Film   = EffectMeta("Retro Film", False, "7034407144908657154", "15206723", "294e09ba63ed72dd245881d516f7a3c6", [
                              EffectParam("effects_adjust_speed", 0.301, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.801, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    Film_Frame_2 = EffectMeta("Film Frame 2", False, "7008413857894896130", "15206722", "fd84488800ef5683555188564886ab76", [])
    Rolling_Film_1 = EffectMeta("Rolling Film", False, "7088226690396066305", "15206743", "19151c1293399104b1aed93d36427182", [
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
    """
    _1998        = EffectMeta("1998", False, "6982772344565535233", "15206774", "d53096e8139dd33f7a2be6adcd7ce56b", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    Reversal_Film = EffectMeta("Reversal Film", False, "7156065656100622849", "15206740", "442b39ec01b7ddefd1a2dfe1ce66d00e", [
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    Leak_2_3     = EffectMeta("Leak 2", False, "7190317638709416449", "9361407", "544b2c0bf76efcafa4c17a7656504262", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.470, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.47, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    Film_2       = EffectMeta("Film 2", False, "6710090540643258891", "15206737", "8a198e87ba4795604c7fe1637d848d4b", [
                              EffectParam("effects_adjust_horizontal_chromatic", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.550, 0.000, 1.000)])
    """参数:
        - effects_adjust_horizontal_chromatic: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.55, 0.00 ~ 1.00
    """
    Glitch       = EffectMeta("Glitch", False, "6707050322696606222", "15206805", "0fb0a4b225be39ca7553d15442ca067a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
    """
    Fuzzy_1      = EffectMeta("Fuzzy", False, "6709706457543086605", "15206813", "467d4eff311315de8fa6549625919286", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    Chromatic_1  = EffectMeta("Chromatic", False, "6709347834690277892", "15206809", "34c4ef20e2bbbc8e16e051ed901c387d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.60, 0.00 ~ 1.00
    """
    Spooky_Camera_1 = EffectMeta("Spooky Camera", False, "7289325398410662401", "103412411", "2c2c06b5bfa714e7dea247d5200d1513", [
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.800, 0.000, 1.000),
                              EffectParam("sticker", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.80, 0.00 ~ 1.00
        - sticker: 默认0.40, 0.00 ~ 1.00
    """
    Level_Glitch_2 = EffectMeta("Level Glitch 2", False, "6815093228216259079", "15206821", "83396b243328eacab9b423ebbb18f36b", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Spooky_Camera_2 = EffectMeta("Spooky Camera", False, "7289325398410662401", "103412411", "2c2c06b5bfa714e7dea247d5200d1513", [
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.800, 0.000, 1.000),
                              EffectParam("sticker", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_sharpen: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.80, 0.00 ~ 1.00
        - sticker: 默认0.40, 0.00 ~ 1.00
    """
    Color_Glitch = EffectMeta("Color Glitch", False, "6915000039609733633", "15206818", "8032aeef1ca2ed78d0e0a2337d1ef042", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Chromozoom   = EffectMeta("Chromo-zoom", False, "6885172354880639490", "15206806", "91376f7887165bb15a4e149dc9be9d9b", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
    """
    XSignal      = EffectMeta("X-Signal", False, "6709706971638927875", "15206808", "ab9776213187c44b3c521b5a7ea6d1df", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    _70s         = EffectMeta("70's", False, "6706773500792689165", "15206819", "d1900db3d7ff04e7903d155114cab1d1", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Distort      = EffectMeta("Distort", False, "6738265357825348103", "15206810", "7bf041bbfb782aba4937b4c439193c65", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Invisible_Person = EffectMeta("Invisible Person", False, "7021892660499583490", "1166234", "2cf16035b605ce73f4b44bcd650adfb3", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.350, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.35, 0.00 ~ 1.00
    """
    Invisible_Person_1 = EffectMeta("Invisible Person", False, "7021892660499583490", "15207025", "2cf16035b605ce73f4b44bcd650adfb3", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.350, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.35, 0.00 ~ 1.00
    """
    Invisible_Person_2 = EffectMeta("Invisible Person", False, "7021892660499583490", "15207025", "2cf16035b605ce73f4b44bcd650adfb3", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.350, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.35, 0.00 ~ 1.00
    """
    Invisible_Person_3 = EffectMeta("Invisible Person", False, "7021892660499583490", "1166234", "2cf16035b605ce73f4b44bcd650adfb3", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.350, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.35, 0.00 ~ 1.00
    """
    Distort_1    = EffectMeta("Distort", False, "6738265357825348103", "15206810", "7bf041bbfb782aba4937b4c439193c65", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    _70s_1       = EffectMeta("70's", False, "6706773500792689165", "15206819", "d1900db3d7ff04e7903d155114cab1d1", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Color_Glitch_2 = EffectMeta("Color Glitch 2", False, "6706773498561319428", "15206820", "c50d8f72262989088d0bc3c9eba4fe17", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    Bad_TV_      = EffectMeta("Bad TV ", False, "6706773499052036615", "15206814", "47c83f6d6073edb2fee0f2d7ee0599a6", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    Snow_Glitch  = EffectMeta("Snow Glitch", False, "6847689727261282824", "15206807", "313fe086202a497cd6941b275e8273de", [
                              EffectParam("effects_adjust_range", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.550, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_noise: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.55, 0.00 ~ 1.00
    """
    Color_Glitch_1 = EffectMeta("Color Glitch", False, "6706773498922013191", "15206811", "73814d72a1a8cba91943394efeda4b34", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.670, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.67, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    Ethereal     = EffectMeta("Ethereal", False, "7021892419763311105", "15207008", "c0bbb93750bb7fe5b9b2900ff853adb6", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    Ethereal_1   = EffectMeta("Ethereal", False, "7021892419763311105", "1166236", "c0bbb93750bb7fe5b9b2900ff853adb6", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    Level_Glitch = EffectMeta("Level Glitch", False, "6806254428358709767", "15206812", "c0895daca20904a1418a5cc257a30d4a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Edgy         = EffectMeta("Edgy", False, "6777238992816443912", "739585", "fd117c14c5deafa6c92d40307f693a15", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.50, 0.00 ~ 1.00
    """
    Ripples      = EffectMeta("Ripples", False, "6940185249749930498", "15206675", "61ab10b10def92e31b0400ac87e43088", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
    """
    Ripple_1     = EffectMeta("Ripple", False, "7173547719485559298", "15206680", "c0db14b731d4f04c95332348a0488089", [
                              EffectParam("effects_adjust_sharpen", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.550, 0.000, 1.000)])
    """参数:
        - effects_adjust_sharpen: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.55, 0.00 ~ 1.00
    """
    Screen_Pulse = EffectMeta("Screen Pulse", False, "7131933214540567042", "15206674", "0736478f60e481067bdeadeb1c620e00", [
                              EffectParam("effects_adjust_speed", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
    """
    Spinning_Space = EffectMeta("Spinning Space", False, "7024402886364762626", "15206677", "ab8caff5408905d424c23bef34af0853", [
                              EffectParam("effects_adjust_size", 0.336, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.667, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.801, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.67, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
    """
    Distorted    = EffectMeta("Distorted", False, "6956102778494128641", "15206678", "14a104e40077679260fa7d622dce5178", [])
    Gentle_Ripples = EffectMeta("Gentle Ripples", False, "7473710408755319297", "1843165631", "3217a5fc43a8a0af877ca1e12220603f", [
                              EffectParam("effects_adjust_distortion", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认0.33, 0.00 ~ 1.00
    """
    Jittered_Ripples_3 = EffectMeta("Jittered Ripples 3", False, "7473710407333450257", "1843165632", "2274d3a9b58ed12ac9a14cde2da41e60", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    White_Diffusion = EffectMeta("White Diffusion", False, "7473710407333499393", "1843165633", "d7c04ac964258cbaeeb82eaee137819a", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Rippling     = EffectMeta("Rippling", False, "7142806548404769281", "15206676", "7a08a3c5aa067e55cd0f638cd3161a1b", [
                              EffectParam("effects_adjust_range", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.350, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.35, 0.00 ~ 1.00
    """
    Jittered_Ripples = EffectMeta("Jittered Ripples", False, "7473710407341838849", "1843165635", "53a125c454b6e1a0b6ab2c2c093f1f5f", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Jittered_Ripples_2 = EffectMeta("Jittered Ripples 2", False, "7473710407337644545", "1843165634", "c4a0883f975f9f935c12e62e43ef9c7b", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Vortex_Setting = EffectMeta("Vortex Setting", False, "6970950464674206210", "15206679", "52e5b1690a75d4e6ca88c7f18f47b7e7", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
    """
    Firefly      = EffectMeta("Firefly", False, "7008482435499299330", "15207140", "811f6c870c1f8f0fc61dd6adc40c71c7", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Firefly_1    = EffectMeta("Firefly", False, "7008482435499299330", "15207140", "811f6c870c1f8f0fc61dd6adc40c71c7", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Heart_Kisses_1 = EffectMeta("Heart Kisses", False, "6925620336390050305", "15207108", "dce0f289716b6e4c4c7256a4ab364188", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Sun          = EffectMeta("Sun", False, "6740540037563159047", "15207136", "a239820b1caf074292fe022c43353a85", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Cherry_Blossom = EffectMeta("Cherry Blossom", False, "6925667539917738497", "1009958", "7372d9708980266944aec9650ccde843", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Rain         = EffectMeta("Rain", False, "6734619419890160131", "15207143", "40a59ce61692a825c049cd5b15bc6ded", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Mist         = EffectMeta("Mist", False, "6733145063997575694", "15207141", "9030b2f627144b2724a3e3881213aeae", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Soft_Rose    = EffectMeta("Soft Rose", False, "6943606244728902145", "1024518", "24c3c52fe9d54c8677ee514c0530528c", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Purple_Mist  = EffectMeta("Purple Mist", False, "6887446089650147841", "15207018", "bf106ce53d50ff0a7ebabe323a69b097", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Flipped_1    = EffectMeta("Flipped", False, "6925617622302069250", "15207107", "d5e216a1700db22637509d2966004b16", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Feathers     = EffectMeta("Feathers", False, "6709706658815152643", "15207001", "2627845c8cff5d5bd99c36aa20f57a11", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Butterfly_Dream_1 = EffectMeta("Butterfly Dream", False, "7013301550458081794", "15206963", "f6829a9af2cd1b32e1aac84543e0931b", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Starry       = EffectMeta("Starry", False, "6734587005872640519", "15207130", "cf7e2f2c81eba90828f32a9f0f99ef5e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Girls_Secrets_1 = EffectMeta("Girl's Secrets", False, "6925618573083677185", "15207106", "ebba75bb53013a6347814b486c6063eb", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    Pink_Hearts  = EffectMeta("Pink Hearts", False, "6792095053360665096", "15207104", "b9b9be20aed7761f81c6757a4428a034", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Luminance    = EffectMeta("Luminance", False, "6966109172001673730", "15207137", "5b7fdba4abb3d3b4fb5a3febe319e999", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.40, 0.00 ~ 1.00
    """
    Fire         = EffectMeta("Fire", False, "6748623656181568011", "15207139", "fc346694609e66fccbc8cf5c171ac14d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Lightning_1  = EffectMeta("Lightning", False, "7104581530567053825", "15207206", "a13ca8bfd8348a04e8d170d16ec8ed16", [
                              EffectParam("effects_adjust_color", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 1.000, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认1.00, 0.00 ~ 1.00
        - sticker: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    Lightning_Crack_1 = EffectMeta("Lightning Crack", False, "7111576355736654337", "15207138", "edd537366858130e593a074d28503dc7", [
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.800, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.80, 0.00 ~ 1.00
        - sticker: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
    """
    Heartbeat_1  = EffectMeta("Heartbeat", False, "6746014633942848007", "15207097", "6d42bba28607f45ca90a7359b7c6ab74", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Camcorder_3  = EffectMeta("Camcorder 3", False, "6894575368624148994", "15207079", "bc759f18216aac435a0cf29b69bb5051", [])
    Camcorder_2  = EffectMeta("Camcorder 2", False, "6720541079080276484", "15207056", "05df74c3ef64c5ec8c97e7fef2caf46f", [])
    BW_VHS       = EffectMeta("B&W VHS", False, "7023733702773445122", "15206997", "1a53630780dee01e236cff7233d35d01", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.530, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.430, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.53, 0.00 ~ 1.00
        - effects_adjust_vertical_chromatic: 默认0.43, 0.00 ~ 1.00
    """
    Camcorder_1  = EffectMeta("Camcorder", False, "6723065859260027403", "15207075", "f05977a18144296bdfa45ca3493d84a9", [])
    Frame_1      = EffectMeta("Frame 1", False, "6709725898762883595", "15206783", "3141b3cd5f3b7f5035020cb6466bfd5b", [
                              EffectParam("effects_adjust_noise", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_noise: 默认1.00, 0.00 ~ 1.00
    """
    Photo_Frame  = EffectMeta("Photo Frame", False, "6839527903424680456", "15207073", "594fd22d6effa8153b7a619746b1dd0f", [])
    Old_TV_2_1   = EffectMeta("Old TV 2", False, "6865921078858879496", "15206785", "62b508cb16fd1c0da7a2989da5bd49fd", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    TV_Lines     = EffectMeta("TV Lines", False, "6763933311933878791", "15206786", "fbf351dd37a0d60885414e3157f838d9", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
    """
    Retro_Cam    = EffectMeta("Retro Cam", False, "6804357689859117581", "15206782", "de0caa2ec7151990960b56f62fedd3fc", [])
    Graphic_3    = EffectMeta("Graphic 3", False, "7005086882442777089", "15207060", "3e38e4db50217711e54dba3a3c284a6e", [])
    Noise        = EffectMeta("Noise", False, "6706773498510971404", "15206769", "3e5fc04a3ddff85aadb6b52681f00bcd", [
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_noise: 默认0.50, 0.00 ~ 1.00
    """
    White_Sprockets = EffectMeta("White Sprockets", False, "6865979592264389127", "15207065", "77fb2991364f2882ef4b61317f7a10dc", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    Insta        = EffectMeta("Insta", False, "6761646727142314509", "15207068", "2a92fcc337bb33af058a2b90b111e704", [])
    Jitter       = EffectMeta("Jitter", False, "6771320983065203213", "15206784", "3d7d53f809b52f7370380f358ef6081c", [
                              EffectParam("effects_adjust_range", 0.250, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.25, 0.00 ~ 1.00
    """
    _1998_1      = EffectMeta("1998", False, "6982772344565535233", "15206774", "d53096e8139dd33f7a2be6adcd7ce56b", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    Constellation = EffectMeta("Constellation", False, "7008480529708225025", "15206656", "1c75b4cf948ba65efeb1af5a25b41a7e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Mini_stars_II = EffectMeta("Mini stars II", False, "6893092073226899970", "15206663", "186c623a413a10ddbf28bfa0215a55f4", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Mini_Stars   = EffectMeta("Mini Stars", False, "6847773569435308558", "15206636", "9f35060cd9e36abab8c5ebb80d8efbf6", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Star_Rain    = EffectMeta("Star Rain", False, "6839514681044898311", "15206648", "620d63550356df332ba5c014b310d6d2", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Daily        = EffectMeta("Daily", False, "6843319885339038216", "15206638", "b692892ba55b4cbd18c97704102b9938", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    Gleam_1      = EffectMeta("Gleam", False, "7176638378056618497", "15206657", "af6015fc0590a70892d5084082fd4490", [
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.55, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_soft: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    Star_Rain_2  = EffectMeta("Star Rain 2", False, "6849588023714124295", "15206634", "5c5349039a938e2348ae58a7dee34302", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Color_Diamond = EffectMeta("Color Diamond", False, "7065581863745622530", "15206664", "a08b91114580a37c9e415aebd62e2b74", [
                              EffectParam("effects_adjust_size", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    Daily_2      = EffectMeta("Daily 2", False, "6843680748856152584", "15206660", "6d80537f452debf98b09f2df79080e37", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    Daily_4      = EffectMeta("Daily 4", False, "6843680812584407559", "15206641", "264fbe6c96d9027b99cd066cad7adc1b", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    Polychromatic = EffectMeta("Polychromatic", False, "7073686283154887170", "15206624", "783debb6f0b544b13113102f74417460", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_number: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    Milky_Way_2  = EffectMeta("Milky Way 2", False, "7011427817090978305", "15206627", "2273947aec8664bd5c7a0f410c8bebfb", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
    """
    Iridescent   = EffectMeta("Iridescent", False, "6778284619499311623", "15206659", "f1c6583c2a7227b6ccf002863fdfdf65", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Torn_Frames  = EffectMeta("Torn Frames", False, "7046710173448016385", "15206721", "1f68be276f639c0246e531b495deeee1", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    Torn_Frames_1 = EffectMeta("Torn Frames", False, "7046710173448016385", "15206715", "9fe5766fed709c36b3885a944ed2596f", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    Torn_Frames_2 = EffectMeta("Torn Frames", False, "7046710173448016385", "1279122", "9fe5766fed709c36b3885a944ed2596f", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    Torn_Frames_3 = EffectMeta("Torn Frames", False, "7046710173448016385", "1279120", "1f68be276f639c0246e531b495deeee1", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    Folds_4      = EffectMeta("Folds 4", False, "6925669248983372289", "15207309", "b04966da3a2bbd9212aec61aaa995c33", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    Blue_Mosaic  = EffectMeta("Blue Mosaic", False, "7131982194070786562", "15207321", "0fceb871b844d51454db5d59da3636ef", [
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    Dot_Silkscreen = EffectMeta("Dot Silkscreen", False, "7148038845286584834", "15207319", "87e58ba33f7dc96c4e108cd67c67e2a4", [
                              EffectParam("effects_adjust_texture", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
    """
    Folds_5      = EffectMeta("Folds 5", False, "6925669391426130433", "15207325", "1530211bc181cd4003243fa6265574db", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    Paper_Tear   = EffectMeta("Paper Tear", False, "6843686214025875981", "15207320", "fd5588f68a681b8eba1449a5d0240097", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    Painting     = EffectMeta("Painting", False, "6808442362314887693", "15207316", "118b5e6a07a603581825a0fa8bb08e35", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    Dot_Silkscreen_1 = EffectMeta("Dot Silkscreen", False, "7148038845286584834", "15207319", "87e58ba33f7dc96c4e108cd67c67e2a4", [
                              EffectParam("effects_adjust_texture", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
    """
    Striped_Glass = EffectMeta("Striped Glass", False, "7003234457519919617", "15207324", "2f5917be32e664eef67419212e54cad0", [
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
    """
    Folds_2      = EffectMeta("Folds 2", False, "6925667720637714946", "15207323", "4efd4758f897b1d364549a688129e5d5", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    Folds_4_1    = EffectMeta("Folds 4", False, "6925669248983372289", "15207309", "b04966da3a2bbd9212aec61aaa995c33", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    Grain        = EffectMeta("Grain", False, "6732693826135134734", "15207311", "3acc0bd2b4264cbf508bd2aa2e4c07dd", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    Old          = EffectMeta("Old", False, "6813924503148564999", "15207318", "473d207c1d0228446726704f0a54bea6", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Folds        = EffectMeta("Folds", False, "6810944968396378638", "15207312", "be4f37157bcaebf356e467050cf11248", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_texture: 默认1.00, 0.00 ~ 1.00
    """
    Energy       = EffectMeta("Energy", False, "6790536507905020430", "15207249", "bac7325acc36e24c3af31df72d5ddaed", [])
    Neon         = EffectMeta("Neon", False, "6795826477590909454", "15207245", "238fbd22ccb939c0b2198e9a6170962d", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Fire_Edges   = EffectMeta("Fire Edges", False, "6803162714148442632", "15207238", "a1aa2a5d030a3e96bc1f3fac839f5b24", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Warning      = EffectMeta("Warning", False, "6956105875241046529", "15207247", "67ed6a4031987dbc9d980102b1faabf7", [])
    BW_Sketch    = EffectMeta("B&W Sketch", False, "6795430643154031111", "15207258", "7f913d28b2a6a7c9f2e2135a54cd78f2", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Quick_Math   = EffectMeta("Quick Math", False, "6956475901471101441", "15207241", "b08f9e05c86b2e980444d336d9db7427", [])
    Flames       = EffectMeta("Flames", False, "6803162375148016135", "15207246", "253bf5ea7d03ec41b60c1837190350e2", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Question_Marks = EffectMeta("Question Marks", False, "6956477260282991105", "15207253", "168794f69f32cdb6011ebca4b5bf3382", [])
    Splice       = EffectMeta("Splice", False, "6795825532668744206", "15207252", "82f7d80616022fb471a047e9bd4c7104", [])
    Mosaic       = EffectMeta("Mosaic", False, "6770564289074827784", "15207266", "c9f3bf5b93d53bdc514be0d9c480fcf0", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    Cartoon_Border = EffectMeta("Cartoon Border", False, "6982880770113147394", "15207263", "96e81364ff14324f55dc61d1a45c30b4", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
    """
    Flames_2     = EffectMeta("Flames 2", False, "6803160938603090440", "15207248", "2f79ecfe12481216bdcfd8ada5bb3afd", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Explosion_2  = EffectMeta("Explosion", False, "6804317747351130638", "15207256", "d642aeba48679e0a96a6a35aeb40eb00", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Super_Like   = EffectMeta("Super Like", False, "7131930924123427329", "15207242", "39e3a29514be39477d164786fb4b3dd0", [
                              EffectParam("effects_adjust_vertical_shift", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_vertical_shift: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
    """
    Oh_My_God    = EffectMeta("Oh My God", False, "7044880135626953218", "15207265", "a6dcf93deb186e86f5a2288855c98d2a", [])
    Dual_Screens = EffectMeta("Dual Screens", False, "6706773500796867075", "15207282", "7850519365aaef0e1d38574238117925", [])
    Four_Screens = EffectMeta("Four Screens", False, "6706773500490682888", "15207284", "5f86df016c27b44bf89d9634c4b1968a", [])
    Three_Screens = EffectMeta("Three Screens", False, "6706773500209664515", "15207277", "ef3bfd8b9fb71755fcba8fcc8359a0f4", [])
    Split_Screen = EffectMeta("Split Screen", False, "7073688311268643330", "15207285", "2eba26aa15c0e44d2c258ce63a38d243", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.100, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.10, 0.00 ~ 1.00
    """
    Trilayer_Mirror_1 = EffectMeta("Tri-layer Mirror", False, "7134537649410281985", "15207281", "26e730a32387f88e9a67c4e8213d9920", [
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    Six_Screens  = EffectMeta("Six Screens", False, "6719657243039502851", "15207283", "fec1efb68fe608dbed22450913e70cc1", [])
    Circuit      = EffectMeta("Circuit", False, "6726773973683540491", "15207278", "ff18dc9f6e55e6a8220d07546677d5b3", [])
    Nine_Screens = EffectMeta("Nine Screens", False, "6719657094741496333", "15207280", "b9598da2197788df869a08ba617b58fd", [])
    Alt_BW       = EffectMeta("Alt. B&W", False, "6719657002571665934", "15207279", "a0a1505a85fbb9b990daf6afdb7291a1", [])
    Snowflakes   = EffectMeta("Snowflakes", False, "6770604155561054734", "739512", "5b1de91c85371d33e408df6eb164e1f8", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Snowflakes_1 = EffectMeta("Snowflakes", False, "6770604155561054734", "15207825", "5b1de91c85371d33e408df6eb164e1f8", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Gold_Sparkles = EffectMeta("Gold Sparkles", False, "7042582968312795650", "15207176", "a552dfa820b5aba27e4f09e3d83b8643", [
                              EffectParam("effects_adjust_speed", 0.336, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Xmas_Stars   = EffectMeta("Xmas Stars", False, "6767219683901837832", "739506", "3e41badb29cc40f017f2ece636d26557", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Xmas_Stars_1 = EffectMeta("Xmas Stars", False, "6767219683901837832", "15207816", "3e41badb29cc40f017f2ece636d26557", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Snowfall     = EffectMeta("Snowfall", False, "6895552379748356609", "15207826", "84aa80de0bf14d5924dab46be29f7b5a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Snowfall_1   = EffectMeta("Snowfall", False, "6895552379748356609", "957029", "84aa80de0bf14d5924dab46be29f7b5a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Fireworks_2_1 = EffectMeta("Fireworks 2", False, "6767147410671014407", "15207172", "7eed03f0203ac3c7dad4a60b433b8af3", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Gold_Sequins = EffectMeta("Gold Sequins", False, "7081821677201396226", "15207174", "767cd468f9dc8d01d3e14fa10fc9b1f4", [
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - sticker: 默认1.00, 0.00 ~ 1.00
    """
    Confetti_II  = EffectMeta("Confetti II", False, "6771299796058640908", "15207179", "098e6d6982f2b6759b61e534573ce001", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Sparkle_Spiral = EffectMeta("Sparkle Spiral", False, "7042583510879572482", "15207177", "14fd0f24372acd5be33505ee5759ca11", [
                              EffectParam("effects_adjust_speed", 0.336, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.34, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Gold_Dust    = EffectMeta("Gold Dust", False, "6709706378702754312", "15207165", "a7078ce916e55b0663390bcef1a5ff1e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Wonderland   = EffectMeta("Wonderland", False, "6763531573594690061", "739757", "d11b0590308cd9e1222de5fd408c95e4", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Wonderland_1 = EffectMeta("Wonderland", False, "6763531573594690061", "15207833", "d11b0590308cd9e1222de5fd408c95e4", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """


class CapCutVideoCharacterEffectType(EffectEnum):
    """CapCut自带的人物特效类型"""

    Woman_4      = EffectMeta("Woman 4", False, "6974274854501487105", "1078798", "c6df976c4473e4b8eeafc25bb4020926", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    Face_Mosaic  = EffectMeta("Face Mosaic", False, "7125730846174089729", "11387787", "a9b6b78a4dcf2486c69a1f52af31ecfc", [
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
    """
    Flipped      = EffectMeta("Flipped", False, "7099699172147728897", "11387804", "5a015d4cb0277db6f8f68ca713f2fe1b", [
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.850, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.85, 0.00 ~ 1.00
    """
    Embarrassed_Face = EffectMeta("Embarrassed Face", False, "7158373935304675841", "11387797", "e40a40c3b1406c65ac02c0d319508e0b", [])
    In_My_Heart  = EffectMeta("In My Heart", False, "7058917667993817601", "11387552", "62cf1078f3a0e623c349cb4200f3de26", [
                              EffectParam("effects_adjust_size", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
    """
    Lightning_Eyes = EffectMeta("Lightning Eyes", False, "7099728025163403778", "11387574", "6b6b4e9eb53581fea08118f62d55c1a9", [
                              EffectParam("effects_adjust_color", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.850, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_filter: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.85, 0.00 ~ 1.00
    """
    Sad          = EffectMeta("Sad", False, "6986527282533765634", "11387823", "0491f6c803d6983d38bd78f401b93168", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - sticker: 默认1.00, 0.00 ~ 1.00
    """
    Totem_Flames = EffectMeta("Totem Flames", False, "7017020143230259713", "11387710", "35e9cbe081d47066558a717ce3a774d8", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    Like         = EffectMeta("Like", False, "7070864738934067713", "11387831", "aef40b9f0ed093f941936ce4e4920d87", [
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_number: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
    """
    Big_Head     = EffectMeta("Big Head", False, "6989976033608864258", "11387796", "7518e7eb3e186350b688bf712b960c97", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
    """
    Electric_Storm = EffectMeta("Electric Storm", False, "7013301476713828866", "11387718", "9a4b3a8a67ed675e0e6820356e03c473", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    Heart_Flames = EffectMeta("Heart Flames", False, "7013302237329887746", "11387704", "a6acb1e8bd33d1fec2ac6a02cd685e1f", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    Electro_Border = EffectMeta("Electro Border", False, "7098986497172312578", "11387614", "d01391f08768383d6115a0b4f297e884", [
                              EffectParam("effects_adjust_color", 0.850, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.400, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.85, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.35, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.40, 0.00 ~ 1.00
    """
    Club_Hearts  = EffectMeta("Club Hearts", False, "7013301512403161601", "11387713", "9908a1656669aadf0d2de2d4935506e2", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    Electric_Shock = EffectMeta("Electric Shock", False, "7013302274994737666", "11387707", "647a269d3f5f8183adb43912d4391397", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    Musical_Notes_2 = EffectMeta("Musical Notes 2", False, "7017019763578638850", "11387735", "d3eeb550f3b10e253d9c6c4a7db9caf4", [])
    Hurricane    = EffectMeta("Hurricane", False, "7017020053962887681", "11387730", "a0bf72f591c6dbba8a211894f618976f", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    Woman_3      = EffectMeta("Woman 3", False, "6974274658174505474", "1078799", "43567fd71493d00bc90873169a742c7b", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    Cool         = EffectMeta("Cool", False, "6989977270966292994", "11387825", "fa8d8ef3f263d4f13327b6bddc10ed0a", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
    """
    Lovestruck   = EffectMeta("Lovestruck", False, "7058954163274650113", "11387557", "2aa9298939a522ca05e5219ab6e91cf6", [
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.80, 0.00 ~ 1.00
    """
    Heart_Background = EffectMeta("Heart Background", False, "7058919499113697793", "11387806", "fabf8aa698dcd25b68894a751b9b2799", [
                              EffectParam("effects_adjust_size", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    Star_Trails  = EffectMeta("Star Trails", False, "7017019840917410306", "11387733", "d53616c1e937c59555dda26f9f606a75", [])
    Cutout_Poster = EffectMeta("Cutout Poster", False, "7141315533768495618", "11387619", "602c047f7cafe02427da4b327fd260cf", [
                              EffectParam("effects_adjust_vertical_chromatic", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.661, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_vertical_chromatic: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_texture: 默认0.66, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    Gorilla_Face = EffectMeta("Gorilla Face", False, "7131932537089167874", "11387798", "d7d8f40a09f8ff9a318cf0ce19b31756", [])
    Big_Mouth    = EffectMeta("Big Mouth", False, "7160946140764967426", "11387795", "e213546a518c747cdf6342e39c1dfbb1", [])
    Tyndall_Effect = EffectMeta("Tyndall Effect", False, "7134538835295212033", "11387577", "b59ac3e268c20a1a82a9d7d0dabf33ff", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    Musical_Notes = EffectMeta("Musical Notes", False, "7017020067153973762", "11387732", "b435f8b5610503a677c487f3aeb47ac7", [])
    Crackling    = EffectMeta("Crackling", False, "7031457001599144450", "11387834", "b3078ea7691c02789dec4360d7ebd5a5", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    Man_4        = EffectMeta("Man 4", False, "6974275526609342977", "1078794", "2ee84c6f69fd3bd4bb081d75862629ee", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    Shape_Trails_2 = EffectMeta("Shape Trails 2", False, "7017020019678646785", "11387736", "e4042d18c205074ab5dee4bf6c19bbbf", [])
    Revolving_Text = EffectMeta("Revolving Text", False, "7090828616589644289", "11387688", "d12c4f42c3cf9dda4af70b8dbcd5b47d", [
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    Streamer_Stroke = EffectMeta("Streamer Stroke", False, "7171360550008394241", "11387618", "43de1121773eea81624460ed929b17e8", [
                              EffectParam("effects_adjust_intensity", 0.850, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.85, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
    """
    Hellfire     = EffectMeta("Hellfire", False, "7017019827709547009", "11387711", "29903a65ede13673b23ac1eedc118b5d", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
    """
    Man_3        = EffectMeta("Man 3", False, "6974275652828533249", "1078793", "a572a62824360ad8c2a73f75751e388a", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    Struck       = EffectMeta("Struck", False, "6989977801239564802", "11387828", "b310c3ede33e6e0819859dbc67ffab7e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.550, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.55, 0.00 ~ 1.00
    """
    Halo_2       = EffectMeta("Halo 2", False, "7013301953312592386", "11387685", "adb70b2ea060371bb7d91ec43c031989", [
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    Chroma_Diffusion = EffectMeta("Chroma Diffusion", False, "7212564583536398850", "19805836", "d37117a77c1710d52e88f5c4320add2e", [
                              EffectParam("effects_adjust_blur", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.650, 0.000, 1.000)])
    """参数:
        - effects_adjust_blur: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_horizontal_chromatic: 默认0.65, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.65, 0.00 ~ 1.00
    """
    Aura         = EffectMeta("Aura", False, "7017019860076990977", "11387715", "d92206d19cb5ae6f8c704fea8639a90a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    Bright_Idea  = EffectMeta("Bright Idea", False, "6989976806040277505", "11387830", "9a0be515180211c4c30a1757d3622ca0", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.600, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认0.60, 0.00 ~ 1.00
        - sticker: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
    """
    Thermal_Aura = EffectMeta("Thermal Aura", False, "7037039160447734274", "11387623", "b578d3e33d8c650dc445c19875f9613f", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.801, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    Radiate_Bolts = EffectMeta("Radiate Bolts", False, "7017020198242750978", "11387694", "4382fab8340a892419f032990d55580b", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
    """
    Mechanical   = EffectMeta("Mechanical", False, "7013301849675534849", "11387706", "66eb2b1b98e4ada7cacba9c39d37be74", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    Dopelgangers = EffectMeta("Dopelgangers", False, "7203239348135793153", "14975252", "dca7518f6eb90654d1c2473406db2890", [
                              EffectParam("effects_adjust_distortion", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    Phantom      = EffectMeta("Phantom", False, "7211359912176128513", "18211955", "6699feabadc4f59732b8087620fc95a6", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    Lightning_Bound = EffectMeta("Lightning Bound", False, "7013301885767520769", "11387712", "d2459fb754b3d9dbb469d29f6af77423", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    Dot_Shadow   = EffectMeta("Dot Shadow", False, "7091594463054664194", "11387607", "ea3cfc504a4f323a6139f768f8c4790c", [
                              EffectParam("effects_adjust_color", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.25, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    Butterfly_Wings = EffectMeta("Butterfly Wings", False, "7013302434449592834", "11387721", "9971f59512aeb3df57cf3fc26a97ae30", [
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    Gas_Flow     = EffectMeta("Gas Flow", False, "7088615910495228418", "11387624", "9b45c0084913ee96062cda0f5b2d978d", [
                              EffectParam("effects_adjust_size", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.670, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.67, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
    """
    Distorted_Whirl = EffectMeta("Distorted Whirl", False, "7264831874311131649", "64450131", "cd94d767b9599d89e59d532a123d8bde", [
                              EffectParam("effects_adjust_color", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.80, 0.00 ~ 1.00
        - effects_adjust_luminance: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_distortion: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Eye_Reflection = EffectMeta("Eye Reflection", False, "7091913595063112194", "11387572", "665fec8aacac1d793e7917a0a0ec3ab3", [
                              EffectParam("effects_adjust_intensity", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.850, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.85, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
    """
    Color_Fringe = EffectMeta("Color Fringe", False, "7013310331942343170", "11387613", "3beec60f57b90ccc2b451a1b5c0152e2", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    Flame_Eyes_  = EffectMeta("Flame Eyes ", False, "7114195261026472449", "11387575", "f540fbe1b2c8581bbbaead29b7f9bceb", [
                              EffectParam("effects_adjust_color", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.15, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.40, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
    """
    Fluoro_Flash = EffectMeta("Fluoro Flash", False, "7099748495032062465", "11387807", "966eed9a941222efd6243c0df6159c59", [
                              EffectParam("effects_adjust_filter", 0.850, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.254, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.85, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.25, 0.00 ~ 1.00
        - sticker: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
    """
    Scan         = EffectMeta("Scan", False, "7017019728266793474", "11387615", "afd1957dbd5f0c371710fc7a92783db9", [
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    Ghost        = EffectMeta("Ghost", False, "7013302010187354625", "11387689", "6cc1df4c330fce3c92fefc89fbe4b7f6", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    Dopelgangers_1 = EffectMeta("Dopelgangers", False, "7203239348135793153", "14975252", "dca7518f6eb90654d1c2473406db2890", [
                              EffectParam("effects_adjust_distortion", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_distortion: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_number: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.00, 0.00 ~ 1.00
    """
    Phantom_1    = EffectMeta("Phantom", False, "7211359912176128513", "18211955", "6699feabadc4f59732b8087620fc95a6", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
    """
    Apparate_1   = EffectMeta("Apparate 1", False, "7203657714084352513", "14996620", "c89c34b83924f3fb5c88f2ece2e095b8", [
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_rotate: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
    """
    Phantom_Face = EffectMeta("Phantom Face", False, "7205784355342389762", "15431153", "327f6afb9dbdd910f127660c1beee71c", [
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_rotate: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_blur: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
    """
    PopOut       = EffectMeta("Pop-Out", False, "7390270123312943617", "404231789", "f36c6922e91c3036495591591aba39d9", [])
    Starlight    = EffectMeta("Starlight", False, "7013302517299679745", "11387696", "cfd7080a8db30efbe03aeafa5d667e22", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    Bubbles_2    = EffectMeta("Bubbles 2", False, "7013302312655393281", "11387723", "baa4deca23e318235dde9d7435ec9923", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    Flame_Wings_1 = EffectMeta("Flame Wings 1", False, "7017020180538593794", "11387728", "bab3b65e0ca81daf7fbef82971d57527", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    Revolving_Flames = EffectMeta("Revolving Flames", False, "7017020163635548673", "11387708", "0336f00d05b706cf8ab9742af8ee16c7", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    Flame_Trails = EffectMeta("Flame Trails", False, "7017019990381433346", "11387737", "8cceb3e50ff34355a70fec18b66e8dd0", [])
    Technology_2 = EffectMeta("Technology 2", False, "7013301347340521985", "11387724", "206a5e4755fd9e0316b179da31b78b27", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    Firework     = EffectMeta("Firework", False, "7017020087890612737", "11387695", "3dc040bd8a6d3853428cc18030e7872a", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
    """
    Halo         = EffectMeta("Halo", False, "7013301917333852674", "11387687", "ce2098aa7d557cfc63d896fc63ec2846", [
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    Gas_Waves    = EffectMeta("Gas Waves", False, "7017020038771118593", "11387686", "d49684beffa531728f6d0b2f5823a465", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
    """
    Sound_Wave   = EffectMeta("Sound Wave", False, "7017019941815587329", "11387698", "029aabdeb9a1f9ea515f8c5891600b90", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    Geometric_Lasers = EffectMeta("Geometric Lasers", False, "7013301777952936449", "11387709", "61e81667f7930fa9f587f23c95f40311", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    Shape_Trails = EffectMeta("Shape Trails", False, "7017019789348442625", "11387734", "1f441482ec9cf28fcf7373dce0c08ceb", [])
    Flame_Wings_2 = EffectMeta("Flame Wings 2", False, "7017019877990863361", "11387701", "93fa02d91dd5f7fd2c41314358ba462d", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    Consciousness = EffectMeta("Consciousness", False, "7013302037655851522", "11387692", "737af2105f0e42907235947e04f1b1d2", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    Looping_Arrows = EffectMeta("Looping Arrows", False, "7013301983549329922", "11387691", "c4543904bdf336051dee6e64c8b5ebdd", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    Scan_2       = EffectMeta("Scan 2", False, "7013302140714095105", "11387617", "994c0cfd5f8fb5fbe0caf76a034f34a6", [
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    Flame_Outline = EffectMeta("Flame Outline", False, "7116774554273321473", "11387609", "c59e7d23c8ce0d8b6e783baaac417c45", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.75, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.30, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.60, 0.00 ~ 1.00
    """
    Color_Fringe_1 = EffectMeta("Color Fringe", False, "7013310331942343170", "11387604", "8ee317d832f1f607777a0491b3d51550", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    Thermal_Aura_2 = EffectMeta("Thermal Aura 2", False, "7037039282812359170", "11387606", "b711586fdabf06e7975e4bc2f2d906e6", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.801, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    Frame_Scatter_2 = EffectMeta("Frame Scatter 2", False, "7013301087172039169", "11387611", "2bc7ecc4b79a372c9fed9a86b850d8a5", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    Frame_Scatter = EffectMeta("Frame Scatter", False, "7013301062400479746", "11387621", "dfce85b57c8054eb4fdc98ea4dc62809", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
    """
    Sinking      = EffectMeta("Sinking", False, "7013302097827336705", "11387625", "521b388b76a4777d0e2fcee81e18ec82", [
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_range: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_color: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Axis_Rotation = EffectMeta("Axis Rotation", False, "7225915491913568770", "26123585", "16c94e8b38c2d306c11b0d4cfb63dec9", [
                              EffectParam("effects_adjust_speed", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_rotate: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
    """
    Light_Trails = EffectMeta("Light Trails", False, "7095687592854688257", "11387573", "864dcb150b85814ca7615946c7265941", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_blur: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.33, 0.00 ~ 1.00
    """
    Speed_Streaks = EffectMeta("Speed Streaks", False, "7013571521624936961", "11387578", "e6c9f05435c8a8912b1321bfa9f39a4a", [
                              EffectParam("effects_adjust_horizontal_shift", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.850, 0.000, 1.000)])
    """参数:
        - effects_adjust_horizontal_shift: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.85, 0.00 ~ 1.00
    """
    Face_Glitch  = EffectMeta("Face Glitch", False, "7251497887199138305", "45805718", "b00871e8d7e141731a2fe3ca29bb857a", [
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_background_animation: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.60, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.50, 0.00 ~ 1.00
    """
    Lightning    = EffectMeta("Lightning", False, "7090049784714629634", "11387571", "9c97ab760617a5c3bc75491b3ad8406b", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000)])
    """参数:
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.10, 0.00 ~ 1.00
        - effects_adjust_intensity: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.70, 0.00 ~ 1.00
    """
    Neon_Doodle  = EffectMeta("Neon Doodle", False, "7111266792927924737", "11387785", "a96b78f7ee84b7cab457a31baf62a4f0", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.220, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.750, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_speed: 默认0.22, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.75, 0.00 ~ 1.00
    """
    Heart_Lenses = EffectMeta("Heart Lenses", False, "7197318181252239874", "12531312", "56f06fc88908e0e8fad7c329bdea3d39", [
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
        - effects_adjust_intensity: 默认0.70, 0.00 ~ 1.00
        - effects_adjust_range: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
    """
    Loving_Gaze  = EffectMeta("Loving Gaze", False, "7058919485608038914", "11387555", "004327d32e6f38279d4f2e6d9d51ae28", [
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.350, 0.000, 1.000)])
    """参数:
        - effects_adjust_filter: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_color: 默认0.00, 0.00 ~ 1.00
        - effects_adjust_speed: 默认1.00, 0.00 ~ 1.00
        - effects_adjust_horizontal_shift: 默认0.50, 0.00 ~ 1.00
        - effects_adjust_vertical_shift: 默认0.35, 0.00 ~ 1.00
    """
    Neon_Variation = EffectMeta("Neon Variation", False, "7114547141300720130", "11387805", "1fca51ec5627ab19543f51e79beeab4d", [
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
        - effects_adjust_speed: 默认0.20, 0.00 ~ 1.00
        - effects_adjust_filter: 默认0.80, 0.00 ~ 1.00
    """
    Woman_2      = EffectMeta("Woman 2", False, "6981654009916428801", "1078802", "6d9b6990df1d66bad249c5defd435576", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    Woman        = EffectMeta("Woman", False, "6981653825182503426", "1078803", "bde6e304a5de9614c0f44644fd3d15be", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    Man          = EffectMeta("Man", False, "6981652541549318657", "1078804", "a6e9afde1f86efbb91c49ecd9d6a8fdc", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
    Man_2        = EffectMeta("Man 2", False, "6981654153042858497", "1078801", "b09c7a6c2134a95aeac139f06217cdde", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
        - effects_adjust_size: 默认0.00, 0.00 ~ 1.00
    """
