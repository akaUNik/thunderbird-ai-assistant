#!/bin/bash
cd thunderbird-extension
zip -r ../thunderbird-ai-assistant.xpi * -x "*.git*" -x "*.DS_Store"