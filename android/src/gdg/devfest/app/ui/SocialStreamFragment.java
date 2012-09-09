package gdg.devfest.app.ui;

import android.webkit.WebView;

/**
 * A {@link WebView}-based fragment that shows Google+ public search results for a given query,
 * provided as the {@link SocialStreamFragment#EXTRA_QUERY} extra in the fragment arguments. If no
 * search query is provided, the conference hashtag is used as the default query.
 *
 * <p>WARNING! This fragment uses the Google+ API, and is subject to quotas. If you expect to
 * write a wildly popular app based on this code, please check the
 * at <a href="https://developers.google.com/+/">Google+ Platform documentation</a> on latest
 * best practices and quota details. You can check your current quota at the
 * <a href="https://code.google.com/apis/console">APIs console</a>.
 */
public class SocialStreamFragment extends com.google.android.apps.iosched.ui.SocialStreamFragment {

    public static final String EXTRA_QUERY = "com.google.android.iosched.extra.QUERY";
    private static final String STATE_POSITION = "position";
    private static final String STATE_TOP = "top";

    private static final long MAX_RESULTS_PER_REQUEST = 20;
    private static final int STREAM_LOADER_ID = 0;

}
