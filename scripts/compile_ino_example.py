#from platformio.builder.tools.pioino import ConvertInoToCpp
import os
Import("env")

custom_example = env.GetProjectOption("custom_example", None)

print("Custom example is: " + str(custom_example))

if custom_example is not None:
    prev_src_dir = env["PROJECT_SRC_DIR"]
    proj_path = env["PROJECT_DIR"]
    # paths are seen as relative from project root location
    example_path = os.path.join(proj_path, custom_example)
    # ConvertToInoCpp() only looks at .ino files from PROJECT_SRC_DIR
    # we temporarily redirect this variable to the examples folder
    env["PROJECT_SRC_DIR"] = example_path
    print("Converting ino for " + example_path)
    env.ConvertInoToCpp()
    env["PROJECT_SRC_DIR"] = prev_src_dir
    # also automatically add to build_src_filter
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
        env["SRC_FILTER"] = "+<*> +<%s>" % example_path
    print("SOURCE FILTER NOW")
    print(env.get("SRC_FILTER", ""))
    # ify ou want to set data/ directory per-example for SPIFFS/LittleFS upload
    #env["PROJECT_DATA_DIR"] = os.path.join(example_path, "data")