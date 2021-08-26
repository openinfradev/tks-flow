FROM alpine/git:v2.30.2
#FROM alpine:3.14

RUN apk add --no-cache curl coreutils bash
#RUN apk add --no-cache libc6-compat

ENV GITHUB_CLI_VERSION 2.0.0

RUN set -ex; \
    curl -L "https://github.com/cli/cli/releases/download/v${GITHUB_CLI_VERSION}/gh_${GITHUB_CLI_VERSION}_checksums.txt" -o checksums.txt; \
    curl -OL "https://github.com/cli/cli/releases/download/v${GITHUB_CLI_VERSION}/gh_${GITHUB_CLI_VERSION}_linux_amd64.tar.gz"; \
    sha256sum --ignore-missing -c checksums.txt; \
    tar xf gh_${GITHUB_CLI_VERSION}_linux_amd64.tar.gz; \
    rm -rf "gh_${GITHUB_CLI_VERSION}_linux_amd64.tar.gz"; \
    cp gh_${GITHUB_CLI_VERSION}_linux_amd64/bin/gh /bin

ENTRYPOINT ["bin/gh"]

