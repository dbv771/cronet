# Copyright (c) 2015 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
    # File lists shared with GN build.
    'media_router_sources': [
      'create_presentation_connection_request.cc',
      'create_presentation_connection_request.h',
      'issue.cc',
      'issue.h',
      'issue_manager.cc',
      'issue_manager.h',
      'issues_observer.h',
      'issues_observer.cc',
      'local_media_routes_observer.cc',
      'local_media_routes_observer.h',
      'media_route.cc',
      'media_route.h',
      'media_router.h',
      'media_router_dialog_controller.cc',
      'media_router_dialog_controller.h',
      'media_router_factory.cc',
      'media_router_factory.h',
      'media_router_metrics.cc',
      'media_router_metrics.h',
      'media_routes_observer.cc',
      'media_routes_observer.h',
      'media_sink.cc',
      'media_sink.h',
      'media_sinks_observer.cc',
      'media_sinks_observer.h',
      'media_source.cc',
      'media_source.h',
      'media_source_helper.cc',
      'media_source_helper.h',
      'presentation_connection_state_observer.cc',
      'presentation_connection_state_observer.h',
      'presentation_media_sinks_observer.cc',
      'presentation_media_sinks_observer.h',
      'presentation_request.cc',
      'presentation_request.h',
      'presentation_service_delegate_impl.cc',
      'presentation_service_delegate_impl.h',
      'presentation_session_messages_observer.cc',
      'presentation_session_messages_observer.h',
      'presentation_session_state_observer.cc',
      'presentation_session_state_observer.h',
      'render_frame_host_id.h',
    ],
    # Files that are only needed on desktop builds
    'media_router_non_android_sources': [
      'media_router_mojo_impl.cc',
      'media_router_mojo_impl.h',
      'media_router_type_converters.cc',
      'media_router_type_converters.h',
    ],
    'media_router_test_support_sources': [
      'media_router_mojo_test.cc',
      'media_router_mojo_test.h',
      'mock_media_router.cc',
      'mock_media_router.h',
      'mock_screen_availability_listener.cc',
      'mock_screen_availability_listener.h',
      'test_helper.cc',
      'test_helper.h',
    ],
  },
}