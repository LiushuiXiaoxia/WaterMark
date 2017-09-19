#!/usr/bin/env sh

tar cvzf deploy/watermark-0.1.tar watermark.*

echo "sha256 watermark-0.1.tar"

shasum -a 256 deploy/watermark-0.1.tar