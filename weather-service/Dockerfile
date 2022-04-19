FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build

WORKDIR /usr/src/core

COPY *.csproj ./
RUN dotnet restore
COPY . .
RUN dotnet publish -c Release -o release

FROM mcr.microsoft.com/dotnet/aspnet:6.0

WORKDIR /usr/src/core
COPY --from=build /usr/src/core/release .

ENTRYPOINT ["dotnet", "weatherservice.dll"]