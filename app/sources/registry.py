from app.sources.adapters.arbeitnow import ArbeitnowSource
from app.sources.adapters.remotive import RemotiveSource
from app.sources.adapters.remoteok import RemoteOKSource


SOURCE_REGISTRY = {
    "remoteok": RemoteOKSource,
    "arbeitnow": ArbeitnowSource,
    "remotive": RemotiveSource,
}