# syntax=docker/dockerfile:1

# Set the Node.js version as a build argument (default: 22.18.0)
ARG NODE_VERSION=22.18.0
ARG NEXT_PUBLIC_BACKEND_URL

# Base image with Node.js and Alpine Linux
FROM node:${NODE_VERSION}-alpine as base
WORKDIR /usr/src/app

ENV NODE_ENV=production

# ---- Dependencies ----
FROM base as deps
COPY package.json package-lock.json ./
RUN --mount=type=cache,target=/root/.npm \
    npm ci --omit=dev

# ---- Build ----
FROM deps as build
ARG NEXT_PUBLIC_BACKEND_URL
ENV NEXT_PUBLIC_BACKEND_URL=${NEXT_PUBLIC_BACKEND_URL}
COPY . .
RUN --mount=type=cache,target=/root/.npm \
    npm ci && npm run build

# ---- Final runtime ----
FROM base as final
ARG NEXT_PUBLIC_BACKEND_URL
ENV NEXT_PUBLIC_BACKEND_URL=${NEXT_PUBLIC_BACKEND_URL}

COPY package.json ./
COPY --from=deps /usr/src/app/node_modules ./node_modules
COPY --from=build /usr/src/app/.next ./.next
COPY --from=build /usr/src/app/public ./public

RUN chown -R node:node /usr/src/app
USER node

EXPOSE 3000

CMD ["npm", "run", "start"]
