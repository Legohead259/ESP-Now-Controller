#from platformio.builder.tools.pioino import ConvertInoToCpp
import os
Import("env")

custom_example = env.GetProjectOption("custom_example", None)

if custom_example is not None:
    print("Custom example is: " + str(custom_example))
    proj_path = env["PROJECT_DIR"]
    # Paths are seen as relative from project root location
    example_path = os.path.join(proj_path, custom_example)
    # Automatically add to build_src_filter
    print("CURRENT SOURCE FILTER")
    print(env.get("SRC_FILTER", ""))
    if "SRC_FILTER" in env:
        # is it a list or a simple string?
        if isinstance(env["SRC_FILTER"], list):
            env["SRC_FILTER"][0] += " +<%s>" % example_path
        else:
            env["SRC_FILTER"] += " +<%s>" % example_path
    else:
        # not set previously:
        env["SRC_FILTER"] = "-<*> +<%s>" % example_path
    print("SOURCE FILTER NOW")
    print(env.get("SRC_FILTER", ""))
    # ify ou want to set data/ directory per-example for SPIFFS/LittleFS upload
    #env["PROJECT_DATA_DIR"] = os.path.join(example_path, "data")